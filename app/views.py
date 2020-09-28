from django.shortcuts import render
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
    return HttpResponse("Hello")

def search(request):
    return HttpResponse("ET ok")