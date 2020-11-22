""" Interface admin """

from django.contrib import admin

from .models import Dosage, Ingredient, Recette

# Main settings
admin.site.site_header = "Agrégateur de recettes"
admin.site.site_title = "Recettes Admin"
admin.site.index_title = (
    "Bienvenue sur l'interface d'administration du site de suggestions recettes."
)

# Dosage
admin.site.register(Dosage)


# Recette
class RecetteIngredientInline(admin.TabularInline):
    """ Détaille les ingredients dans chaque recette """

    model = Dosage  # the query goes through an intermediate table.
    extra = 0
    verbose_name = "Ingrédient"
    verbose_name_plural = "Ingrédients"

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "ingredient":
            kwargs["queryset"] = Ingredient.objects.order_by("name")
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Recette)
class RecetteAdmin(admin.ModelAdmin):
    """Interface admin pour les recettes"""

    inlines = [
        RecetteIngredientInline,
    ]
    list_display = ["name", "active", "description", "veggie", "categorie"]
    list_filter = ["active", "categorie"]
    list_editable = ("description",)
    search_fields = [
        "name",
        "description",
    ]
    actions = [
        "approve_recipe",
        "reject_recipe",
        "class_recipe_desert",
        "class_recipe_dish",
    ]

    # Moderation
    def approve_recipe(self, request, queryset):
        """ Approve plusieurs recette à la fois"""
        queryset.update(active=True)

    approve_recipe.short_description = "✅ Accepter recette"

    def reject_recipe(self, request, queryset):
        """ Rejette plusieurs recettes à la fois """
        queryset.update(active=False)

    reject_recipe.short_description = "❌ Cacher recette"

    def class_recipe_desert(self, request, queryset):
        """ Classe plusieurs recettes à la fois en dessert """
        queryset.update(desert=True)

    class_recipe_desert.short_description = "🍰 Marquer comme étant un dessert"

    def class_recipe_dish(self, request, queryset):
        """ Classe plusieurs recettes à la fois en plat """
        queryset.update(desert=False)

    class_recipe_dish.short_description = "🍲 Marquer comme étant un plat"


class RecettesPourCetIngredientInline(admin.TabularInline):
    """ Détaille les ingredients dans chaque recette """

    model = Dosage  # the query goes through an intermediate table.
    extra = 0
    verbose_name = "Ingrédient"
    readonly_fields = ("recette",)
    fields = ["recette", "quantite", "unite", "displayed"]
    can_delete = False


# Ingredient
@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """ Interface admin pour les ingrédients """

    list_display = ["name", "categorie", "nb_recettes"]
    list_editable = ("categorie",)
    list_filter = ("categorie",)
    search_fields = ["name"]

    inlines = [
        RecettesPourCetIngredientInline,
    ]
