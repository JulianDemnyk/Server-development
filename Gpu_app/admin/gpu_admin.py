from django.contrib import admin
from Gpu_app.models.gpu_main import GpuMain


@admin.register(GpuMain)
class GpuMainAdmin(admin.ModelAdmin):
    list_display = ('gpu_name', 'gpu_manufacturer', 'gpu_series', 'gpu_ram', 'gpu_ram_type', 'gpu_description')
