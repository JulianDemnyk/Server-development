from django.contrib import admin
from Powersupply_app.models import PowerSupply_main


@admin.register(PowerSupply_main)
class PowerSupplyAdmin(admin.ModelAdmin):
    list_display = ('powersupply_name', 'powersupply_manufacturer', 'powersupply_power', 'powersupply_description')
