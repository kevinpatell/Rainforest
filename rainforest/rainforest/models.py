from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=225)
    descriptiion = models.TextField()
    price_in_cents = models.IntegerField()

    def __str__(self):
        return (self.name)