from django.contrib import admin
from .models import car

# Register your models here.
class CarAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'car_type')

admin.site.register(car, CarAdmin)