from django.db import models
from parts.models import Motherboard, Cpu, Gpu, Ram, Memory, Psu


# Create your models here.

class BuildPC(models.Model):
    motherboard = models.ForeignKey(Motherboard, on_delete=models.SET(None))
    cpu = models.ForeignKey(Cpu, on_delete=models.SET(None))
    gpu = models.ForeignKey(Gpu, on_delete=models.SET(None))
    ram = models.ForeignKey(Ram, on_delete=models.SET(None))
    mem = models.ForeignKey(Memory, on_delete=models.SET(None))
    psu = models.ForeignKey(Psu, on_delete=models.SET(None))