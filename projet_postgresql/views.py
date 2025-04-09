# views.py

from rest_framework import viewsets, filters
from .models import Produit
from .serializers import ProduitSerializer

class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nom', 'description']

