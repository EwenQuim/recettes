# Generated by Django 3.1.1 on 2020-10-06 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0021_auto_20201006_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recette',
            name='preparation_time',
            field=models.PositiveSmallIntegerField(default=15),
        ),
    ]
