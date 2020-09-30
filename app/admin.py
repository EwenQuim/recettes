from django.contrib import admin
from .models import Recette, Ingredient

# Register your models here.
admin.site.register(Ingredient)

class RecetteIngredientInline(admin.TabularInline):
    model = Ingredient.recettes.through # the query goes through an intermediate table.
    extra = 0
    verbose_name = "Ingrédient"
    verbose_name_plural = "Ingrédients"

@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    inlines = [RecetteIngredientInline,]
