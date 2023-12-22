from django.contrib.auth.models import User
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='Supply_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.name

