from django.contrib import admin
from projet_postgresql.models import Produit
# Register your models here.
# admin.site.register(Produit)

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    search_fields = ['nom', 'description']
    list_display = ['nom', 'prix', 'latitude', 'longitude']