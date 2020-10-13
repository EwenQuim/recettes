"""
Computing things (mostly the recommendation system)
"""

import random

from .models import Dosage, Recette


def list_ingredients(recette: Recette):
    """
    Take a Recette object and returns a list
    Each element is a dict [<name>, <quantity>, <unit>, ... (more to come)]
    """
    return Dosage.objects.filter(recette=recette.pk)

    # USEFUL FOR LATER ?
    # unique_ingredient = {
    #     "name" = d.ingredient, # works bcause of __str__
    #     "quantite" = d.quantite,
    #     "unite" = d.unite
    # }


# def compute_day_from_week(week, **options):

#     return random.randint(1, 10)


def compute_missing_meals_from(week):
    """
    Given a int list, compute missing recipes according to some options
    """
    recettes = Recette.objects.filter(active=True, desert=False)
    meals = []
    for _, meal in zip(range(len(week)), week):
        if meal == 0:
            meals.append(random.choice(recettes))
        else:
            meals.append(Recette.objects.get(pk=meal))
    return meals
