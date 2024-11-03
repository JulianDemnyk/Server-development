from django.contrib import admin
from Cpu_app.models import Cpu_main  # Переконайтеся, що імпорт правильний


@admin.register(Cpu_main)
class CpuAdmin(admin.ModelAdmin):
    list_display = ('cpu_name', 'cpu_manufacturer', 'cpu_series', 'cpu_socket', 'cpu_cores', 'cpu_threads', 'cpu_tdp', 'cpu_description')
