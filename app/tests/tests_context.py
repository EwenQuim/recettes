"""Tests the context sent to the templates
"""

from django.test import TestCase

from app.context import context_liste


class ContextCase(TestCase):
    """Class to test the context generator"""

    def test_context_liste(self):

        liste_generated = context_liste({"viande": (50, "g"), "poireau": (2, "u")})

        liste_expected = [
            {"name": "poireau", "quantite": 2, "unite": "u"},
            {"name": "viande", "quantite": 50, "unite": "g"},
        ]
        self.assertEqual(liste_generated["liste"], liste_expected)
