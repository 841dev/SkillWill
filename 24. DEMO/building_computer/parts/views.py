from django.shortcuts import render
from rest_framework import generics
from .models import Motherboard
from .serializers import Motherboardserializer
from rest_framework.permissions import IsAdminUser
# Create your views here.


class MotherboardListView(generics.ListAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = Motherboardserializer

class MotherboardCreateView(generics.ListCreateAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = Motherboardserializer
    permission_classes = [IsAdminUser]

class MotherboardUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = Motherboardserializer
    lookup_field = 'pk'

class MotherboardDeleteView(generics.RetrieveDestroyAPIView):
    queryset = Motherboard.objects.all()
    serializer_class = Motherboardserializer
    lookup_field = 'pk'