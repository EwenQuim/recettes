from django.db import models

# Create your models here.
class Recette(models.Model):
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=150, default="Description rapide et alléchante!")
    description = models.TextField()

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    vegetarian = models.BooleanField(default=False)
    recettes = models.ManyToManyField(Recette, related_name='recettes', blank=True, through='Dosage')

    def __str__(self):
        return self.name

class Dosage(models.Model):
    recette = models.ForeignKey(Recette, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.IntegerField()

    class Unites(models.TextChoices):
        g = 'g', 'grammes'
        mL = 'mL', 'millilitres'
        cas = 'cas', 'cuillère à soupe'
        cac = 'cac', 'cuillère à cafe'
        p = 'pincee', 'pincée'
        t = 't', 'tranches'
        u = '.', 'unite'

    unite = models.CharField(max_length=20, choices=Unites.choices, default=Unites.g)