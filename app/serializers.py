"""Serializers"""
from rest_framework import serializers

from .models import Recette


class RecetteSerializer(serializers.ModelSerializer):
    """Serializer : public fields

    Args:
        serializers ([type]): [description]
    """

    class Meta:
        """
        Fields selected that are public for reading and writing (GET and POST)
        """

        fields = (
            "id",
            "name",
            "description",
            "veggie",
            "instructions",
            "categorie",
            "pour",
            "cooking_time",
            "image",
            "image_web",
        )
        model = Recette
