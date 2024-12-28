from django.db import models
from country.models import Country


class Activity(models.Model):
    name = models.CharField(max_length=100)
    cities = models.ManyToManyField(
        Country,
        related_name="activities",
    )
    price_person = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.CharField(max_length=100)
    gps = models.CharField(max_length=100)
    note = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name
