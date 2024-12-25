from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    note = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name