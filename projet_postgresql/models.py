from django.db import models
from pgvector.django import VectorField
from django.contrib.gis.geos import Point
from django.contrib.gis.db import models as gis_models
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    prix = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    localisation = gis_models.PointField(null=True, blank=True)
    vector_search = VectorField(dimensions=384, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Génère la localisation si elle n’est pas définie
        if not self.localisation and self.latitude and self.longitude:
            self.localisation = Point(self.longitude, self.latitude)  # lon, lat

        # Génère le vecteur si non défini
        if self.vector_search is None:
            text = f"{self.nom} {self.description}"
            self.vector_search = model.encode(text).tolist()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nom