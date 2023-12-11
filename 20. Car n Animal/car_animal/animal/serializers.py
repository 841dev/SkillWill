from . models import animal

from rest_framework import serializers

class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = animal
        fields = '__all__'  # as well as ['', '', '']
