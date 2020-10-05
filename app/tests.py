from django.test import TestCase
from app.models import Recette, Ingredient, Dosage

class RecetteTestCase(TestCase):

    def setUp(self):
        instructions = "- Faire ceci \
                        - Faire cela"
        Recette.objects.create(name="Pates Pesto", description="La recette des pâtes pesto!", instructions=instructions, active=True)
        
        Ingredient.objects.create(name="Pates", categorie="feculent")
        Ingredient.objects.create(name="Pesto", categorie="sauce")


    def test_get_object(self):
        pates_pesto = Recette.objects.get(name="Pates Pesto")
        self.assertEqual(pates_pesto.description, "La recette des pâtes pesto!")

    # def test_if_is_vegetarian_from_list(self):
    #     pates_pesto = Recette.objects.get(name="Pates Pesto")
    #     self.assertEqual(pates_pesto.veggie(), True)

