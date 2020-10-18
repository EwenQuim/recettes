from django.test import TestCase

from app.compute import compute_missing_meals_from, compute_recipe_dict
from app.models import Dosage, Ingredient, Recette


class RecetteModelCase(TestCase):
    @classmethod
    def setUp(self):
        # Recettes
        instructions = "- Faire ceci \
                        - Faire cela"
        self.pates_pesto = Recette.objects.create(
            name="Pates Pesto",
            description="La recette des pâtes pesto!",
            instructions=instructions,
            active=True,
        )

        self.bolo = Recette.objects.create(
            name="Pates Bolo",
            description="Les pâtes bolo c'est mieux!",
            instructions=instructions,
            active=True,
        )

        # Ingredients
        self.pates = Ingredient.objects.create(name="Pates", categorie="feculent")
        self.pesto = Ingredient.objects.create(name="Pesto", categorie="sauce")

        self.hache = Ingredient.objects.create(name="Viande Hachée", categorie="viande")
        self.tomat = Ingredient.objects.create(name="Tomate", categorie="legume")

        # Dosages
        Dosage.objects.create(
            recette=self.pates_pesto, ingredient=self.pates, quantite=200, unite="g"
        )
        Dosage.objects.create(
            recette=self.pates_pesto, ingredient=self.pesto, quantite=20, unite="mL"
        )

        Dosage.objects.create(
            recette=self.bolo, ingredient=self.hache, quantite=2, unite="g"
        )
        Dosage.objects.create(
            recette=self.bolo, ingredient=self.tomat, quantite=2, unite="g"
        )

    def test_compute_missing_meals_from(self):
        """Tests if it can compute the meal from a given list"""
        meals = compute_missing_meals_from([2, 1])
        self.assertEqual(meals, [self.bolo, self.pates_pesto])

    def test_compute_recipe_dict(self):
        recipe = {
            "Pates": (200, "g"),
            "Pesto": (20, "mL"),
        }
        recipe_computed = compute_recipe_dict([self.pates_pesto])

        self.assertEqual(recipe, recipe_computed)
