from django.db import models

# Create your models here.
class animal(models.Model):
    species = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    weight = models.FloatField()
