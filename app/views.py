from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Recette, Dosage, Ingredient

# Create your views here.
def index(request):
    context = {"foo": "Fbedjsfnjkqfs"}
    return render(request, "app/index.html", context)


def listing(request):
    context = {}
    context["recettes"] = Recette.objects.all()
    return render(request, "app/listing.html", context)


def detail(request, recette_id):
    # Getting recipe
    recette = get_object_or_404(Recette, pk=recette_id)

    # Getting ingredients
    ingredients = []
    for d in Dosage.objects.filter(recette_id=recette.id):
        for i in Ingredient.objects.filter(id=d.ingredient_id):
            ingredients.append(i)
    context = {
        "recette": recette,
        "ingredients": ingredients
    }
    return render(request, "app/details.html", context)


def search(request):
    return HttpResponse("ET ok")