from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    calories = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    in_stock = models.BooleanField(default=True)