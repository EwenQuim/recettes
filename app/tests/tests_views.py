"""Testing the views of the app"""

from django.test import TestCase
from django.urls import reverse

from .tests_models import RecetteModelCase


class RecetteViewsTest(TestCase):
    """Testing the views of the app"""

    @classmethod
    def setUp(self):
        RecetteModelCase.setUp()

    def test_view_url_exists_at_desired_location(self):
        """self-explanatory"""
        response = self.client.get("/recettes/")
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """self-explanatory"""
        response = self.client.get(reverse("app:index"))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """self-explanatory"""
        response = self.client.get(reverse("app:recettes"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "app/listing/listing.html")

    def test_view_detail(self):
        """self-explanatory"""
        response = self.client.get("/recettes/" + "1", follow=True)
        self.assertEqual(response.status_code, 200)
