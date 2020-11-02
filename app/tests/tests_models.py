"""Tests the models of the application
"""

from django.test import TestCase

from app.models import Dosage, Ingredient, Recette


class RecetteModelCase(TestCase):
    """Class for testing the models and data"""

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

    def test_get_object(self):
        """Tests if the object created can be accessed"""
        pates_pesto = Recette.objects.get(name="Pates Pesto")
        self.assertEqual(pates_pesto.description, "La recette des pâtes pesto!")

    def test_if_is_vegetarian_from_list(self):
        """Test if a Recette is vegetarian or not"""
        pates_pesto = Recette.objects.get(name="Pates Pesto")
        self.assertTrue(pates_pesto.veggie())

        pates_bolo = Recette.objects.get(name="Pates Bolo")
        self.assertFalse(pates_bolo.veggie())

    def test_names(self):
        """Test names displaying"""
        self.assertEqual(str(self.bolo), "Pates Bolo")
        self.assertEqual(str(self.pesto), "Pesto")
