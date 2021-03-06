# Generated by Django 3.1.1 on 2020-09-30 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_ingredient_recettes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantite', models.IntegerField()),
                ('unite', models.CharField(choices=[('g', 'grammes'), ('mL', 'millilitres'), ('cas', 'cuillère à soupe'), ('cac', 'cuillère à cafe'), ('pincee', 'pincée')], default='g', max_length=20)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.ingredient')),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.recette')),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='recettes',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='recettes',
            field=models.ManyToManyField(blank=True, related_name='recettes', through='app.Dosage', to='app.Recette'),
        ),
    ]
