# Generated by Django 3.1.1 on 2020-10-04 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_ingredient_categorie'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='vegetarian',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='categorie',
            field=models.CharField(choices=[('legume', '🥕 Légume'), ('fruit', '🍒 Fruit'), ('viande', '🍗 Viande'), ('poisson', '🐟 Poisson'), ('laitage', '🥛 Laitage'), ('boisson', '🍺 Boisson'), ('autre', '⭐️ Autre'), ('inconnu', '❌ Inconnu')], default='inconnu', max_length=25),
        ),
    ]