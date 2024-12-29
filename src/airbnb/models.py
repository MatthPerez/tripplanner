from django.db import models
from django.utils.timezone import now
from country.models import Country

class Airbnb(models.Model):
    name = models.CharField(max_length=50)
    reference = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    charges = models.DecimalField(max_digits=6, decimal_places=2)
    cities = models.ManyToManyField(
        Country,
        related_name="airbnbs",
    )
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)

    def __str__(self):
        return self.name