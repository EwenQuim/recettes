# Generated by Django 3.1.1 on 2020-09-30 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_dosage_unite'),
    ]

    operations = [
        migrations.AddField(
            model_name='dosage',
            name='unite',
            field=models.CharField(choices=[('g', 'grammes'), ('mL', 'millilitres'), ('cas', 'cuillère à soupe'), ('cac', 'cuillère à cafe'), ('pincee', 'pincée')], default='g', max_length=20),
        ),
    ]
