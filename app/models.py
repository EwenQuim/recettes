"""Defines models, aka the database structure
    """

from django.db import models


# Create your models here.
class Recette(models.Model):
    """Recette : represents a recipe, the core of the website"""

    class Categorie(models.TextChoices):
        """self-explanatory"""

        entree = "entree", "Entrée"
        plat = "plat", "Plat"
        dessert = "dessert", "Dessert"

    # Model Methods
    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()

    def veggie(self):
        """Self-explanatory. Just call

        bolognese.veggie() == False,
        ratatouille.veggie() == True

        Returns:
            [bool]
        """

        for ingredient in self.ingredients.all():
            if (ingredient.categorie == "viande") or (
                ingredient.categorie == "poisson"
            ):
                return False
        return True

    veggie.boolean = True
    veggie.short_description = "Végé ?"

    name = models.CharField(
        verbose_name="Nom",
        unique=True,
        max_length=100,
        help_text='Concis. Pas de "recette originale" ou autre style.',
    )
    description = models.CharField(
        max_length=150,
        help_text="Description rapide et alléchante ! Style libre",
        blank=True,
    )
    instructions = models.TextField()
    active = models.BooleanField(default=False)

    categorie = models.CharField(
        max_length=25, choices=Categorie.choices, default=Categorie.plat
    )
    pour = models.PositiveSmallIntegerField(default=2)
    cooking_time = models.PositiveSmallIntegerField(
        verbose_name="Temps passé en cuisine",
        default=15,
        help_text="Temps total (cuisson + préparation)",
    )
    ponderation = models.PositiveSmallIntegerField(
        default=3, help_text="1 : rare / 5 : fréquemment recommandé"
    )
    difficulty = models.PositiveSmallIntegerField(
        verbose_name="Difficulté", default=3, help_text="1 : facile / 5 : dur"
    )
    image = models.CharField(
        max_length=100,
        help_text="url de l'image à afficher, \
            stockée en local (recette ajoutée par le bot)",
        default="empty",
    )
    image_web = models.CharField(
        max_length=100,
        help_text="url à afficher, si l'image n'est pas disponible \
            sur le serveur",
        default=(  # Placeholder
            "https://paleomg.com/wp-content/plugins/simple-recipe-pro\
            /assets/placeholder.png",
        ),
    )


class Ingredient(models.Model):
    """Modelling a single ingredient and its properties"""

    class Categorie(models.TextChoices):
        """self-explanatory"""

        legumes = "legume", "🥕 Légume"
        fruit = "fruit", "🍒 Fruit"
        feculent = "feculent", "🌾 Féculent"
        epice = "epice", "🌶 Épice"
        viande = "viande", "🍗 Viande"
        poisson = "poisson", "🐟 Poisson"
        laitage = "laitage", "🥛 Laitage"
        sucre = "sucre", "🍬 Sucré"
        sauce = "sauce", "🥣 Sauce"
        pain = "pain", "🥖 Pain"
        autre = "autre", "⭐️ Autre"
        inconnu = "inconnu", "❌ Inconnu"

    # Model Methods
    def __str__(self):
        return self.name

    def clean(self):
        self.name = self.name.capitalize()

    def nb_recettes(self):
        """Returns the number of recipes in which there is the ingredient"""
        return self.recettes.count()

    nb_recettes.short_description = "Recettes"

    # Model Fields
    name = models.CharField(
        max_length=100,
        unique=True,
        help_text="Concis. Majuscule seulement au début.",
    )
    recettes = models.ManyToManyField(
        Recette, related_name="ingredients", blank=True, through="Dosage"
    )
    categorie = models.CharField(
        max_length=25, choices=Categorie.choices, default=Categorie.inconnu
    )


class Dosage(models.Model):
    """The quantity of each ingredient for a given recipe"""

    class Unites(models.TextChoices):
        """self-explanatory"""

        g = "g", "grammes"
        mL = "ml", "millilitres"
        cas = "cas", "cuillère à soupe"
        cac = "cac", "cuillère à cafe"
        p = "pincee", "pincée"
        t = "t", "tranches"
        u = "u", "unite"

    # Model Methods
    def __str__(self):
        return self.displayed

    # Model Fields
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.IntegerField()
    unite = models.CharField(max_length=20, choices=Unites.choices, default=Unites.u)
    displayed = models.CharField(max_length=200, blank=True)
