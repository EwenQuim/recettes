from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recette, Dosage, Ingredient
from .compute import compute_missing_meals_from

# Create your views here.
def index(request):
    context = {"foo": "bar"}
    return render(request, "app/index.html", context)

def about(request):
    return render(request, "app/about.html")

def listing(request):
    recettes = Recette.objects.filter(active=True)
    context = {"recettes": recettes}
    return render(request, "app/listing.html", context)


def detail(request, recette_id):
    # Getting Recette
    recette = get_object_or_404(Recette, pk=recette_id)

    # Getting Ingredients & dosages, formatted
    ingredients_displayed = []

    for d in Dosage.objects.filter(recette_id=recette.id):

        ingredients_displayed.append(d.displayed)
        
    context = {"recette": recette, "ingredients_displayed": ingredients_displayed}
    return render(request, "app/details.html", context)


def search(request):
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
        
        context = {"recettes": recettes, "title":title}

    return render(request, "app/listing.html", context)

def suggestion(request, monAM=0, monPM=0, tueAM=0, tuePM=0, wedAM=0, wedPM=0, thuAM=0, thuPM=0, friAM=0, friPM=0, satAM=0, satPM=0, sunAM=0, sunPM=0):
    
    week = [ monAM, monPM, tueAM, tuePM, wedAM, wedPM, thuAM, thuPM, friAM, friPM, satAM, satPM, sunAM, sunPM]

    options = {
        "veggie": False
    }

    meals = compute_missing_meals_from(week, options)

    print(meals)

    context = {
        "week": meals,
        "weekDays": "Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche".split(),
        "generatedUrl": "-".join(map(lambda meal: str(meal.id), meals)).strip(),
    }
    return  render(request, "app/suggest.html", context)
