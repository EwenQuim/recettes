"""Tests the parser
"""

from django.test import TestCase

from app.parser import parse_slug


class ParserCase(TestCase):
    """Class to test the parsings"""

    def test_parse_slug(self):
        """Tests if it can compute the meal from a given list"""
        parsed = parse_slug("6-3-0-4-5")
        self.assertEqual(parsed, [6, 3, 0, 4, 5] + ([0] * 9))
