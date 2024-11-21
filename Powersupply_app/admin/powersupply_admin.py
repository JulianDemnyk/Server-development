from django.contrib import admin
from Powersupply_app.models.powersupply_main import PowerSupplyMain


@admin.register(PowerSupplyMain)
class PowerSupplyMainAdmin(admin.ModelAdmin):
    list_display = ('powersupply_name', 'powersupply_manufacturer', 'powersupply_power', 'powersupply_description')
