""" Compute the context (to send to the template) from given variables
"""


def context_suggestion(meals):
    """Compute the context for the weekly suggestion

    Args:
        meals (Recette list): recipe list

    Returns:
        dict: self-explainatory
    """
    # Deduce unique url
    meals_int_list = list(map(lambda meal: str(meal.id), meals))
    # Displayed lines
    week_days = "Lundi Mardi Mercredi Jeudi Vendredi Samedi Dimanche".split()
    url = "-".join(meals_int_list)
    # We need an iterable for the "FOR" loop
    iterable_week = []
    for i in range(14):
        # Url for change
        list_adapted_for_meal_change = [*meals_int_list]
        list_adapted_for_meal_change[i] = "0"
        url_unique_meal = "-".join(list_adapted_for_meal_change)

        # Displayed
        suffix = " soir" if (i % 2) else " midi"
        iterable_week.append(
            {
                "mealName": week_days[i // 2] + suffix,
                "recette": meals[i],
                "urlChangeMeal": url_unique_meal,
            }
        )

    return {
        "week": iterable_week,
        "generatedUrl": url,
    }


def context_liste(dico_ingredients):
    """
    Given a {"recipe": (quantity, unit)} dict, returns a [Ingredient, quantity, unit] list
    """
    liste_plate = []
    for k, value in dico_ingredients.items():
        line = {"name": k, "quantite": value[0], "unite": value[1]}
        if value[0] == 0:
            liste_plate.append(line)
        else:
            liste_plate = [line] + liste_plate
    return {"liste": liste_plate}
