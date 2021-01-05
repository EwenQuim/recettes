# Generated by Django 3.1.1 on 2020-11-03 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0031_auto_20201103_1732"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recette",
            name="preparation_time",
        ),
        migrations.AddField(
            model_name="recette",
            name="cooking_time",
            field=models.PositiveSmallIntegerField(
                default=15, help_text="Temps total (cuisson + préparation"
            ),
        ),
        migrations.AlterField(
            model_name="recette",
            name="difficulte",
            field=models.PositiveSmallIntegerField(
                default=3, help_text="1 : facile / 5 : dur"
            ),
        ),
        migrations.AlterField(
            model_name="recette",
            name="ponderation",
            field=models.PositiveSmallIntegerField(
                default=3, help_text="1 : rare / 5 : fréquent"
            ),
        ),
    ]
