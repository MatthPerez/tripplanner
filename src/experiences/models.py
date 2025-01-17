from django.db import models


class Experience(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField(max_length=100)
    note = models.TextField(max_length=255, null=True)

    def __str__(self):
        return self.name
