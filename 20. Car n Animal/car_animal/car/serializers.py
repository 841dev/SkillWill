from . models import car

from rest_framework import serializers

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = '__all__'  # as well as ['', '', '']
