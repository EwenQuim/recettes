# Generated by Django 3.1.1 on 2020-10-08 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0023_recette_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosage',
            name='displayed',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='recette',
            name='description',
            field=models.CharField(blank=True, help_text='Description rapide et alléchante!', max_length=150),
        ),
    ]
