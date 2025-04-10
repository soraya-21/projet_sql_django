# Generated by Django 4.2.20 on 2025-04-09 12:45

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import pgvector.django.vector


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Produit",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nom", models.CharField(max_length=255)),
                ("description", models.CharField(max_length=255)),
                ("prix", models.FloatField()),
                ("latitude", models.FloatField()),
                ("longitude", models.FloatField()),
                (
                    "localisation",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                (
                    "vector_search",
                    pgvector.django.vector.VectorField(
                        blank=True, dimensions=384, null=True
                    ),
                ),
            ],
        ),
    ]
