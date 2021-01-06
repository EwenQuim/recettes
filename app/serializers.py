from rest_framework import serializers
from .models import Recette


class RecetteSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            "id",
            "name",
            "description",
            "veggie",
            "instructions",
            "active",
            "categorie",
            "pour",
            "cooking_time",
            "image",
            "image_web",
        )
        model = Recette