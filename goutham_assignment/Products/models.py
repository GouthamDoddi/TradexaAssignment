from django.db import models
from django.utils import timezone


class Product(models.Model):
    name = models.CharField(max_length=65)
    weight = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(timezone.now())
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
