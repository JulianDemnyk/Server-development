from django.contrib import admin
from Cpu_app.models.cpu_main import CpuMain


@admin.register(CpuMain)
class CpuMainAdmin(admin.ModelAdmin):
    list_display = ('cpu_name', 'cpu_manufacturer', 'cpu_series', 'cpu_socket', 'cpu_cores', 'cpu_threads', 'cpu_tdp', 'cpu_description')
