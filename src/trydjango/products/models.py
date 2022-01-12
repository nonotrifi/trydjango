from django.db import models

class Product(models.Model):
    titre = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    prix = models.DecimalField(decimal_places=2, max_digits=100)
    sommaire = models.TextField(blank=False, null=False)
    featured = models.BooleanField() # null=True, default=True
# Create your models here.
