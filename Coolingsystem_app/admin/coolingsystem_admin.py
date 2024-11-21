from django.contrib import admin
from Coolingsystem_app.models.coolingsystem_main import CoolingSystemMain


@admin.register(CoolingSystemMain)
class CoolingSystemMainAdmin(admin.ModelAdmin):
    list_display = ('coolingsystem_name', 'coolingsystem_manufacturer', 'coolingsystem_form_factor', 'coolingsystem_tdp', 'coolingsystem_description')