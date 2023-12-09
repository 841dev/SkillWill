from django.template import loader

from django.shortcuts import render
from django.http import HttpResponse
from reader.forms import Readers_Data

# Create your views here.

def reader(request):
    if request.method == 'POST':
        form = Readers_Data(request.POST)
        if form.is_valid():
            return render(request, 'book.html')


    return render(request, 'reader.html', {"form" : Readers_Data})
