from django.urls import path

from . import views # import views so we can use them in urls.

app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('recettes/<int:recette_id>/', views.detail, name="detail"),
    path('recettes/search/', views.search, name="recherche"),
    path('recettes/', views.listing, name="recettes"),
]