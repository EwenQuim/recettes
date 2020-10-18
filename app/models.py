"""Defines models, aka the database structure
    """

from django.db import models


# Create your models here.
class Recette(models.Model):
    """Recette : represents a recipe, the core of the website"""

    name = models.CharField(
        verbose_name="Nom",
        unique=True,
        max_length=100,
        help_text="Concis. Majuscule seulement au début.",
    )
    description = models.CharField(
        max_length=150, help_text="Description rapide et alléchante!", blank=True
    )
    instructions = models.TextField()
    active = models.BooleanField(default=False)
    desert = models.BooleanField(verbose_name="Dessert", default=False)
    pour = models.PositiveSmallIntegerField(default=2)
    preparation_time = models.PositiveSmallIntegerField(default=15)
    image = models.CharField(
        max_length=100,
        help_text="url de l'image à afficher. Est stockée en local.",
        default="empty",
    )

    def veggie(self):
        """Self-explanatory. Just call

        bolognese.veggie() == False,
        ratatouille.veggie() == True

        Returns:
            [bool]
        """
        for dosage in Dosage.objects.filter(recette_id=self.id):
            for ingredient in Ingredient.objects.filter(id=dosage.ingredient_id):
                if (ingredient.categorie == "viande") or (
                    ingredient.categorie == "poisson"
                ):
                    return False
        return True

    veggie.boolean = True
    veggie.short_description = "Végé ?"

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    """Modelling a single ingredient and its properties"""

    name = models.CharField(max_length=100, unique=True)
    recettes = models.ManyToManyField(
        Recette, related_name="ingredients", blank=True, through="Dosage"
    )

    class Categorie(models.TextChoices):
        """self-explanatory"""

        legumes = "legume", "🥕 Légume"
        fruit = "fruit", "🍒 Fruit"
        feculent = "feculent", "🌾 Féculent"
        epice = "epice", "🌶 Épice"
        viande = "viande", "🍗 Viande"
        poisson = "poisson", "🐟 Poisson"
        laitage = "laitage", "🥛 Laitage"
        sucre = "sucre", "🍬 Sucre"
        sauce = "sauce", "🥣 Sauce"
        autre = "autre", "⭐️ Autre"
        inconnu = "inconnu", "❌ Inconnu"

    categorie = models.CharField(
        max_length=25, choices=Categorie.choices, default=Categorie.inconnu
    )

    def __str__(self):
        return self.name


class Dosage(models.Model):
    """The quantity of each ingredient for a given recipe"""

    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    displayed = models.CharField(max_length=200, blank=True)

    class Unites(models.TextChoices):
        """self-explanatory"""

        g = "g", "grammes"
        mL = "ml", "millilitres"
        cas = "cas", "cuillère à soupe"
        cac = "cac", "cuillère à cafe"
        p = "pincee", "pincée"
        t = "t", "tranches"
        u = "u", "unite"

    unite = models.CharField(max_length=20, choices=Unites.choices, default=Unites.u)
