from django.contrib import admin
from Coolingsystem_app.models import CoolingSystem_main


@admin.register(CoolingSystem_main)
class CoolingSystemAdmin(admin.ModelAdmin):
    list_display = ('coolingsystem_name', 'coolingsystem_manufacturer', 'coolingsystem_form_factor', 'coolingsystem_tdp', 'coolingsystem_description')