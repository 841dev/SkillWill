from django.http import HttpResponse
from django.shortcuts import render
from .models import user
import datetime

# Create your views here.

def user_data(request):
    f_name = user.objects.all().values()[0].get('first_name')
    l_name = user.objects.all().values()[0].get('last_name')
    birth = user.objects.all().values()[0].get('birth_date')
    birth_year = user.objects.all().values()[0].get('birth_date').year

    this_year = int(datetime.date.today().strftime('%Y'))

    age = this_year-birth_year
    return HttpResponse(f"First name: {f_name}, "
                        f"Last name: {l_name}, "
                        f"Birthday: {birth}   "
                        f"AGE:  {age}")
