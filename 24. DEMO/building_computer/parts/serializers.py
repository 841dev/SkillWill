from rest_framework import serializers
from .models import Motherboard


class Motherboardserializer(serializers.ModelSerializer):
    class Meta:
        model = Motherboard
        fields = ['brand',
                  'model',
                  'chipset',
                  'cpu_compatibility',
                  'cpu_socket',
                  'integrated_gpu',
                  'ram_slots',
                  'usb_slots']

