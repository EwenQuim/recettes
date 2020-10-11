from django.urls import reverse, reverse_lazy
from django.test import TestCase

from app.models import Recette, Dosage, Ingredient
from .tests_models import RecetteModelCase

class RecetteViewsTest(TestCase):

    @classmethod
    def setUp(self):
        RecetteModelCase.setUp()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get("/recettes/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse("app:recettes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/listing.html")

    def test_view_detail(self):
        response = self.client.get("/recettes/" + "1", follow=True)
        print("\nPRINT")
        print(response["location"])

        self.assertEqual(response.status_code, 200)
