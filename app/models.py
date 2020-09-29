from django.db import models

# Create your models here.
class Recette(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    short = models.CharField(max_length=150, default="Description rapide et alléchante!")
    description = models.TextField()

    def __str__(self):
        return self.name
