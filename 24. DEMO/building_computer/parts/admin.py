from django.contrib import admin
from .models import Motherboard, Cpu, Gpu, Ram, Memory, Psu
from .models import MemoryImage
from .forms import MemoryForm
from django.utils.safestring import mark_safe



class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'cpu_compatibility')
    list_filter = ('brand', 'cpu_compatibility', 'cpu_socket')
    list_display_links = ('id', 'brand', 'model')
    list_per_page = 20
    list_max_show_all = 100

admin.site.register(Motherboard, MotherboardAdmin)

class CpudAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'cpu_socket', 'core_quantity', 'thread_quantity', 'cpu_speed')
    list_filter = ('brand', 'cpu_socket')
    list_display_links = ('id', 'brand', 'model')
    list_per_page = 20
    list_max_show_all = 100

admin.site.register(Cpu, CpudAdmin)

class GpuAdmin(admin.ModelAdmin):
    list_display = ('id', 'vga_brand', 'model', 'memory_amount', 'gpu_speed', 'memory_speed')
    list_filter = ('vga_brand', 'gpu_brand')
    list_display_links = ('id', 'vga_brand', 'model',)
    #list_editable = ('memory_amount', 'gpu_speed',)
    list_max_show_all =100
    #change_list_template =

admin.site.register(Gpu, GpuAdmin)


class RamAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'memory_type', 'memory_amount', 'memory_speed', 'memory_kit')
    list_display_links = ('id', 'brand', 'model')
    list_filter = ('brand', 'memory_type', 'memory_amount', 'memory_kit')

admin.site.register(Ram, RamAdmin)

"""class ImageInlineAdmin(admin.StackedInline):
    model = MemoryImage
    form = MemoryForm"""
class MemoryAdmin(admin.ModelAdmin):
    #inlines = [ImageInlineAdmin]
    list_display = ('id', 'brand', 'model', 'memory_type', 'slot_type', 'memory_amount', 'img_preview', 'image')
    list_filter = ('brand', 'memory_type', 'slot_type')
    list_display_links = ('id', 'brand', 'model')
    readonly_fields = ['img_preview']


admin.site.register(Memory, MemoryAdmin)
#admin.site.register(ImageInlineAdmin)


class PsuAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', 'watt', 'premium_quality')
    list_display_links = ('id', 'brand', 'model')
    list_filter = ('brand', 'watt', 'premium_quality')

admin.site.register(Psu, PsuAdmin)