from django.contrib import admin
from .models import Recette, Ingredient

# Register your models here.
admin.site.register(Recette)
admin.site.register(Ingredient)