"""
Views: from arguments, return something to insert in a template.
Mostly calling to the database and apply the right compute functions
"""
from django.shortcuts import get_object_or_404, render

from .compute import compute_missing_meals_from, compute_recipe_list
from .context import context_liste, context_suggestion
from .models import Dosage, Ingredient, Recette
from .parser import parse_slug


# Create your views here.
def index(request):
    """Returns the main view, at /
    TODO make it more friendly
    """
    context = {"foo": "bar"}
    return render(request, "app/index.html", context)


def about(request):
    """Display some information
    - Security
    - Privacy
    - Open-source & algorithm
    - me ?
    """
    return render(request, "app/about.html")


def listing(request):
    """Lists all accepted recipe"""
    recettes = Recette.objects.filter(active=True)
    context = {"recettes": recettes}
    return render(request, "app/listing/listing.html", context)


def detail(request, recette_id):
    """Display the details and instructions
    Given the recipe id
    """
    # Getting Recette
    recette = get_object_or_404(Recette, pk=recette_id)

    # Getting Ingredients & dosages, formatted
    ingredients_displayed = map(
        lambda dosage: dosage.displayed, Dosage.objects.filter(recette_id=recette.id)
    )

    context = {"recette": recette, "ingredients_displayed": ingredients_displayed}
    return render(request, "app/details.html", context)


def search(request):
    """The search query"""
    query = request.GET.get("query")
    if not query:
        context = {"recettes": Recette.objects.all()}
    else:
        title = f"Résultats pour : {query}"

        # Getting recipe by name
        recettes = Recette.objects.filter(name__icontains=query)

        # By description
        recettes = recettes.union(Recette.objects.filter(description__icontains=query))

        # By instructions
        recettes = recettes.union(Recette.objects.filter(instructions__icontains=query))

        # By ingredients
        ingredients_identifies = Ingredient.objects.filter(name__icontains=query)
        for i in ingredients_identifies:
            recettes = recettes.union(i.recettes.all())

        context = {"recettes": recettes, "title": title}

    return render(request, "app/listing/listing.html", context)


def suggestion(request, slug=("0-" * 14)[:-1]):
    """is capable of generating random recipe (according to some parameters)
    given a list on already known meals (id > 0)
    where the id = 0
    """
    week_numbers = parse_slug(slug)

    if week_numbers:  # slug understandable

        # Compute meals
        # options = {"veggie": False}
        meals = compute_missing_meals_from(week_numbers)

        liste_course = compute_recipe_list(meals)

        context = context_suggestion(meals)
        context |= context_liste(liste_course)
        return render(request, "app/suggestions/suggest.html", context)

    return render(request, "500.html")
