from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MaxLengthValidator #testing
from django.utils.html import mark_safe
#from django.utils.safestring import mark_safe



class Motherboard(models.Model):
    cpu_brands = (
        ('intel', 'Intel'),
        ('amd', 'AMD')
    )
    cpu_sockets = (
        ('LGA 775', 'LGA 775'),
        ('lga_1150', 'LGA 1150'),
        ('lga_1151', 'LGA 1151'),
        ('lga_1200', 'LGA 1200'),
        ('lga_1700', 'LGA 1700'),
        ('lga_2011', 'LGA 2011'),
        ('lga_2011_v3', 'LGA 2011-v3'),
        ('lga_2066', 'LGA 2066'),
        ('lga_4677', 'LGA 4677'),

        ('fm2+', 'FM2+'),
        ('am4', 'AM4'),
        ('am5', 'AM5'),
        ('tr4', 'TR4'),
        ('trx4', 'TRX4'),
        ('strx4', 'sTRX4'),
        ('str5', 'sTR5')
    )
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50, unique=True)
    chipset = models.CharField(max_length=20)
    cpu_compatibility = models.CharField(max_length=10, choices=cpu_brands)
    cpu_socket = models.CharField(max_length=12, choices=cpu_sockets)
    integrated_gpu = models.BooleanField(null=False, default=False)
    ram_slots = models.PositiveIntegerField(default=2, validators=[MaxValueValidator(12)])
    usb_slots = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.brand} - {self.model} - {self.cpu_socket}"


class Cpu(models.Model):
    cpu_brands = (
        ('Intel', 'Intel'),
        ('amd', 'AMD')
    )
    cpu_sockets = (
        ('lga_1150', 'LGA 1150'),
        ('lga_1151', 'LGA 1151'),
        ('lga_1200', 'LGA 1200'),
        ('lga_1700', 'LGA 1700'),
        ('lga_2011', 'LGA 2011'),
        ('lga_2011_v3', 'LGA 2011-v3'),
        ('lga_2066', 'LGA 2066'),
        ('lga_4677', 'LGA 4677'),

        ('fm2+', 'FM2+'),
        ('am4', 'AM4'),
        ('am5', 'AM5'),
        ('tr4', 'TR4'),
        ('trx4', 'TRX4'),
        ('strx4', 'sTRX4'),
        ('str5', 'sTR5')
    )
    brand = models.CharField(max_length=20, choices=cpu_brands)
    model = models.CharField(max_length=50, unique=True)
    cpu_socket = models.CharField(max_length=12, choices=cpu_sockets)
    core_quantity = models.PositiveIntegerField(default=2)
    thread_quantity = models.PositiveIntegerField(default=2)
    cpu_speed = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.cpu_socket}"

class Gpu(models.Model):
    gpu_brands = (
        ('nvidia', 'Nvidia'),
        ('ati', 'ATI')
    )
    vga_brands = (
        ('nvidia', 'Nvidia'),
        ('ati', 'ATI'),
        ('asus', 'ASUS'),
        ('msi', 'MSI'),
        ('sapphire', 'SAPPHIRE'),
        ('evga', 'EVGA')
    )
    vga_brand = models.CharField(default='nvidia', max_length=10, choices=vga_brands)
    model = models.CharField(max_length=50, unique=True)
    gpu_brand = models.CharField(default='nvidia', max_length=10, choices=gpu_brands)
    memory_amount = models.PositiveIntegerField()
    gpu_speed = models.FloatField(validators=[MinValueValidator(0.0)])
    memory_speed = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.vga_brand} - {self.model}"

class Ram(models.Model):
    mem_type = (
        ('ddr1','DDR1'),
        ('ddr2','DDR2'),
        ('ddr3','DDR3'),
        ('ddr4','DDR4'),
        ('ddr5','DDR5')
    )
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50, unique=True)
    memory_type = models.CharField(max_length=10, choices=mem_type)
    memory_amount = models.PositiveIntegerField()
    memory_kit = models.BooleanField(default=True)
    memory_speed = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.brand} - {self.model} - {self.memory_amount} GB"

class Memory(models.Model):
    mem_type = (
        ('hdd','HDD'),
        ('ssd','SSD'),
        ('nvme','NVMe')
    )
    slt_type = (
        ('pata','PATA'),
        ('sata','SATA'),
        ('pcie','PCIe'),
        ('m.2','M.2')
    )
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    memory_type = models.CharField(max_length=5, choices=mem_type)
    slot_type = models.CharField(max_length=5, choices=slt_type)
    memory_amount = models.PositiveIntegerField()
    image = models.ImageField(upload_to="images/memory", null=True, help_text='helptext')
    def __str__(self):
       return f"{self.brand} - {self.model} - {self.memory_amount} GB"

    def img_preview(self):  # new
        if self.image:
            return mark_safe(f'<img src = "{self.image.url}" width = "100"/>')
        else:
            return 'No Image Found'



class MemoryImage(models.Model):
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/memory')


class Psu(models.Model):
    brand = models.CharField(max_length=20)
    model = models.CharField(max_length=50, unique=True)
    watt = models.PositiveIntegerField()
    premium_quality = models.BooleanField(null=False)

    def __str__(self):
        return f"{self.brand} - {self.model}"


"""class Computer(models.Model):
    motherboar = models.ForeignKey(Motherboard, on_delete=models.SET(None))
    cpu = models.ForeignKey(Cpu, on_delete=models.SET(None))
    gpu = models.ForeignKey(Gpu, on_delete=models.SET(None))
    ram = models.ForeignKey(Ram, on_delete=models.SET(None))
    memory = models.ForeignKey(Memory, on_delete=models.SET(None))
    psu = models.ForeignKey(Psu, on_delete=models.SET(None))
"""