from django.db import models


# Create your models here.
class Dog(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
