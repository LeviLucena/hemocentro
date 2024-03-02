# Generated by Django 5.0.1 on 2024-02-29 22:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("estoque", "0007_alter_estoquesangue_options_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="estoquesangue",
            name="bolsas_coletadas",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="estoquesangue",
            name="bolsas_utilizadas",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="estoquesangue",
            name="data",
            field=models.DateField(default=datetime.date.today),
        ),
    ]
