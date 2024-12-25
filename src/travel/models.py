from django.db import models
from django.utils.timezone import now

class Travel(models.Model):
    date = models.DateField(default=now)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    start_place = models.CharField(max_length=100)
    start_time = models.CharField(max_length=5)
    end_place = models.CharField(max_length=100)
    end_time = models.CharField(max_length=5)
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.start_place
    