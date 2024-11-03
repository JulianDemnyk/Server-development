from django.contrib import admin
from Gpu_app.models import Gpu_main


@admin.register(Gpu_main)
class GpuAdmin(admin.ModelAdmin):
    list_display = ('gpu_name', 'gpu_manufacturer', 'gpu_series', 'gpu_ram', 'gpu_ram_type', 'gpu_description')
