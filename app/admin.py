from django.contrib import admin
from .models import Recette, Ingredient, Dosage

# Main settings
admin.site.site_header = "Agrégateur de recettes"
admin.site.site_title = "Recettes Admin"
admin.site.index_title = "Bienvenur sur l'interface d'administration du site de suggestions recettes. Réalisé par Ewen Quimerc'h"

# Recette
class RecetteIngredientInline(admin.TabularInline):
    model = Ingredient.recettes.through # the query goes through an intermediate table.
    extra = 0
    verbose_name = "Ingrédient"
    verbose_name_plural = "Ingrédients"

@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    inlines = [RecetteIngredientInline,]
    list_display = ['name', 'active', 'description','veggie']
    list_filter = ['active']
    search_fields = ['name', 'description',]
    actions = ['approve_recipe', 'reject_recipe']

    # Moderation
    def approve_recipe(self, request, queryset):
        queryset.update(active=True)
    approve_recipe.short_description = "✅ Accepter recette"

    def reject_recipe(self, request, queryset):
        queryset.update(active=False)
    reject_recipe.short_description = "❌ Cacher recette"

# Ingredient
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ['name', 'categorie']
    list_filter = ('categorie',)
    list_editable = ('categorie',)
    search_fields = ['name']