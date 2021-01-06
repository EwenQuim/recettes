"""Views for the API"""
import random

from rest_framework import generics

from .serializers import RecetteSerializer
from .models import Recette


class ListRecipe(generics.ListCreateAPIView):
    """
    Generates list of all recipe
    """

    queryset = Recette.objects.all()
    serializer_class = RecetteSerializer


class RandomRecipe(generics.ListCreateAPIView):
    """
    Gives a random recipe
    """

    #pks = Recette.objects.values_list("pk", flat=True)
    #random_pk = random.choice(pks)
    serializer_class = RecetteSerializer

    def get_queryset(self):
        """
        Returns first of a random list
        """
        return [Recette.objects.order_by("?").first()]
