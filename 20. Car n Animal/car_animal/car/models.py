from django.db import models

# Create your models here.
class car(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    car_type = models.CharField(max_length=20)
