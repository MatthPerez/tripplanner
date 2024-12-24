from django.db import models
from django.utils.timezone import now

class Airbnb(models.Model):

    name = models.CharField(
        max_length=50,
    )
    reference = models.CharField(
        max_length=20,
    )
    price = models.IntegerField(
        max_length=4,
    )
    charges = models.IntegerField(
        max_length=4,
    )
    city = models.CharField(
        max_length=50,
    )
    start_date = models.DateField(default=now)
    end_date = models.DateField(default=now)

    def __str__(self):
        return self.name
