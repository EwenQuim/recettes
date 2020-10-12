# Generated by Django 3.1.1 on 2020-10-12 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0026_auto_20201009_1013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='unite',
            field=models.CharField(choices=[('g', 'grammes'), ('ml', 'millilitres'), ('cas', 'cuillère à soupe'), ('cac', 'cuillère à cafe'), ('pincee', 'pincée'), ('t', 'tranches'), ('u', 'unite')], default='u', max_length=20),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='recettes',
            field=models.ManyToManyField(blank=True, related_name='ingredients', through='app.Dosage', to='app.Recette'),
        ),
    ]
