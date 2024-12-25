from django.db import models

class Expense(models.Model):
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    category = models.IntegerField(max_length=100)
    price = models.IntegerField(max_length=4)
    note = models.TextField(max_length=100, null=True)

    def __str__(self):
        return self.name