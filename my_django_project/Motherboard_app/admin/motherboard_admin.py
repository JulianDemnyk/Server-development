from django.contrib import admin
from Motherboard_app.models import Motherboard_main


@admin.register(Motherboard_main)
class MotherboardAdmin(admin.ModelAdmin):
    list_display = ('motherboard_name', 'motherboard_manufacturer', 'motherboard_socket_motherboard','motherboard_sata_slot', 'motherboard_m2_slot', 'motherboard_ram_type', 'motherboard_description', 'motherboard_form_factor')
