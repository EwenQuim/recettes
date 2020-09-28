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

def detail(request, recette_id):
    question = get_object_or_404(Recette, pk=recette_id)
    return render(request, 'polls/detail.html', {'question': question})

def search(request):
    return HttpResponse("ET ok")