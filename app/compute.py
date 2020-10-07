from django.shortcuts import get_object_or_404

from .models import Recette, Ingredient, Dosage

def list_ingredients(recette: Recette):
    # Take a Recette object and returns a list
    # Each element is a dict [<name>, <quantity>, <unit>, ... (more to come)]
    return Dosage.objects.filter(recette=recette.pk)

        # USEFUL FOR LATER ?
        # unique_ingredient = {
        #     "name" = d.ingredient, # works bcause of __str__
        #     "quantite" = d.quantite,
        #     "unite" = d.unite
        # }
