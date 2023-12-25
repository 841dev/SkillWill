from django.contrib import admin
from .models import  BuildPC

# Register your models here.

class BuildPCAdmin(admin.ModelAdmin):
    list_display = ('id', 'motherboard', 'cpu', 'gpu', 'ram', 'mem', 'psu')

admin.site.register(BuildPC, BuildPCAdmin)