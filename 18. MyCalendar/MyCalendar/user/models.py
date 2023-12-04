from django.db import models

# Create your models here.

class user(models.Model):
    first_name = models.CharField(max_length=20, null=False)
    last_name = models.CharField(max_length=30, null=False)
    birth_date = models.DateField(null=False)


