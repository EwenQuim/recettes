from django.urls import reverse, reverse_lazy
from django.test import TestCase

from .models import Recette, Dosage, Ingredient

class RecetteViewsTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/recettes/')
        self.assertEqual(response.status_code, 200)
           
    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('app:index'))
        self.assertEqual(response.status_code, 200)
        
    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('app:recettes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app/listing.html')