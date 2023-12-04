from django.http import HttpResponse
from django.shortcuts import render
from .models import user

# Create your views here.

def user_data(request):
    users = user.first_name()
    return HttpResponse(first_name)