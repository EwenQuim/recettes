from django.test import TestCase

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
        pates = Ingredient.objects.create(name="Pates", categorie="feculent")
        pesto = Ingredient.objects.create(name="Pesto", categorie="sauce")

        hache = Ingredient.objects.create(name="Viande Hachée", categorie="viande")
        tomat = Ingredient.objects.create(name="Tomate", categorie="legume")

        # Dosages
        Dosage.objects.create(
            recette=self.pates_pesto, ingredient=pates, quantite=200, unite="g"
        )
        Dosage.objects.create(
            recette=self.pates_pesto, ingredient=pesto, quantite=20, unite="mL"
        )

        Dosage.objects.create(
            recette=self.bolo, ingredient=hache, quantite=2, unite="g"
        )
        Dosage.objects.create(
            recette=self.bolo, ingredient=tomat, quantite=2, unite="g"
        )

    def test_get_object(self):
        pates_pesto = Recette.objects.get(name="Pates Pesto")
        self.assertEqual(pates_pesto.description, "La recette des pâtes pesto!")

    def test_if_is_vegetarian_from_list(self):
        pates_pesto = Recette.objects.get(name="Pates Pesto")
        self.assertTrue(pates_pesto.veggie())

        pates_bolo = Recette.objects.get(name="Pates Bolo")
        self.assertFalse(pates_bolo.veggie())
