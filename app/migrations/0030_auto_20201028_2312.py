# Generated by Django 3.1.1 on 2020-10-28 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0029_auto_20201028_2258"),
    ]

    operations = [
        migrations.AlterField(
            model_name="ingredient",
            name="name",
            field=models.CharField(
                help_text="Concis. Majuscule seulement au début.",
                max_length=100,
                unique=True,
            ),
        ),
    ]