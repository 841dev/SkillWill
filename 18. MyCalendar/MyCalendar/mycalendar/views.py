from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def date(request):
    d = datetime.date.today()

    return HttpResponse(f"Today is:  {d.strftime('%Y')} "
                        f"{d.strftime('%B')} "
                        f"{d.strftime('%d')}"
                        f" {d.strftime('%A')}")