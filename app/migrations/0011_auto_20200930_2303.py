# Generated by Django 3.1.1 on 2020-09-30 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_dosage_unite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dosage',
            name='unite',
            field=models.CharField(choices=[('g', 'grammes'), ('mL', 'millilitres'), ('cas', 'cuillère à soupe'), ('cac', 'cuillère à cafe'), ('pincee', 'pincée'), ('t', 'tranches'), ('.', 'unite')], default='g', max_length=20),
        ),
    ]
