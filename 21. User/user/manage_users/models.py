from django.db import models

# Create your models here.

class Users(models.Model):
    f_name = models.CharField(max_length=20, null=False)
    l_name = models.CharField(max_length=20, null=False)
    mail = models.EmailField(max_length=30)
