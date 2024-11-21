from django.contrib import admin
from Ram_app.models.ram_main import RamMain


@admin.register(RamMain)
class RamMainAdmin(admin.ModelAdmin):
    list_display = ('ram_name', 'ram_manufacturer', 'ram_form_factor', 'ram_size', 'ram_amount', 'ram_description')
