from django.urls import path

from . import views # import views so we can use them in urls.

app_name = 'app'

urlpatterns = [
    path('', views.index, name="index"),
    path('a-propos', views.about, name="about"),
    path('recettes/<int:recette_id>/', views.detail, name="detail"),
    path('recettes/search/', views.search, name="recherche"),
    path('recettes/', views.listing, name="recettes"),
    path('suggestion/', views.suggestion, name="suggestion"),
    path('suggestion/<int:monAM>-<int:monPM>-<int:tueAM>-<int:tuePM>-<int:wedAM>-<int:wedPM>-<int:thuAM>-<int:thuPM>-<int:friAM>-<int:friPM>-<int:satAM>-<int:satPM>-<int:sunAM>-<int:sunPM>', views.suggestion, name="suggestion"),
]