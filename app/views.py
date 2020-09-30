from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render
from .models import Recette

# Create your views here.
def index(request):
    context = { "foo": "Fbedjsfnjkqfs" }
    return render(request, 'app/index.html', context)

def listing(request):
    context = {}
    context["recettes"] = Recette.objects.all()
    return render(request, 'app/listing.html', context)

def detail(request, id):
    recette = get_object_or_404(Recette, pk=id)
    return render(request, 'app/details.html', {'recette': recette})

def search(request):
    return HttpResponse("ET ok")