# Generated by Django 3.1.1 on 2020-10-04 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_auto_20201004_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='name',
            field=models.CharField(help_text='Concis. Majuscule seulement au début.', max_length=100, verbose_name='Nom'),
        ),
    ]
