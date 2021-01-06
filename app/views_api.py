from .serializers import RecetteSerializer
from .models import Recette
from rest_framework import generics
import random


class ListRecipe(generics.ListCreateAPIView):
    """Generates list of all recipe"""

    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer


class RandomRecipe(generics.ListCreateAPIView):
    """Gives a random recipe"""

    pks = Recette.objects.values_list("pk", flat=True)
    random_pk = random.choice(pks)
    serializer_class = RecetteSerializer

    def get_queryset(self):
        return [Recette.objects.order_by("?").first()]
