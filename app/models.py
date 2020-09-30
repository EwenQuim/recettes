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
    recettes = models.ManyToManyField(Recette, related_name='recettes', blank=True)

    def __str__(self):
        return self.name