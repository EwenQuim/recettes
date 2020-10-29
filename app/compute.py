"""
Computing things (mostly the recommendation system)
"""

import random

from .models import Dosage, Recette


def compute_all_recipe():
    """Everyday it's shuffling

    Returns:
        Randomly ordered queryset of active recipes !
    """
    return Recette.objects.filter(active=True).order_by("?")


def compute_missing_meals_from(week, time=None, diff=None, veggie=None):
    """
    Given a int list, compute missing recipes according to some options
    """

    veggie = veggie == "on"
    print(time, diff)

    recettes = list(Recette.objects.filter(active=True, categorie="plat"))

    if veggie:
        recettes = [recette for recette in recettes if recette.veggie()]

    meals = []
    for _, meal in zip(range(len(week)), week):
        if meal == 0:
            meals.append(random.choice(recettes))
        else:
            meals.append(Recette.objects.get(pk=meal))
    return meals


def compute_recipe_dict(meals):
    """
    Given the meals, returns a {"ingredient.name": (quantity, unit)} dict
    """
    dico_ingredients = {}
    for meal in meals:
        ingredients = meal.ingredients.all()
        for ingredient in ingredients:
            dosage = Dosage.objects.filter(recette=meal, ingredient=ingredient).first()
            if ingredient.name not in dico_ingredients:
                dico_ingredients[ingredient.name] = (dosage.quantite, dosage.unite)
            else:
                dico_ingredients[ingredient.name] = (
                    dico_ingredients[ingredient.name][0] + dosage.quantite,
                    dico_ingredients[ingredient.name][1],
                )
    return dico_ingredients
