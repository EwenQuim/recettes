from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recette, Dosage, Ingredient
from .compute import list_ingredients
from .parsing import parse_ingredient_line

# Create your views here.
def index(request):
    context = {"foo": "Fbedjsfnjkqfs"}
    return render(request, "app/index.html", context)


def listing(request):
    recettes = Recette.objects.filter(active=True)
    context = {"recettes": recettes, "title": ""}
    return render(request, "app/listing.html", context)


def detail(request, recette_id):
    # Getting Recette
    recette = get_object_or_404(Recette, pk=recette_id)

    # Getting Ingredients & dosages, formatted
    ingredients_displayed = []

    for d in Dosage.objects.filter(recette_id=recette.id):

        ingredients_displayed.append(d.displayed)
        
    context = {"recette": recette, "ingredients_displayed": ingredients_displayed}
    print(ingredients_displayed)
    return render(request, "app/details.html", context)


def search(request):
    query = request.GET.get("query")
    if not query:
        recettes = Recette.objects.all()
    else:
        recettes = Recette.objects.filter(name__icontains=query)
    if not recettes.exists():
        recettes = Recette.objects.filter(description__icontains=query)

    for r in recettes:
        print("\n\n", list_ingredients(r))
    title = f"Résultats pour : {query}"
    context = {"recettes": recettes, "title": title}
    return render(request, "app/listing.html", context)
