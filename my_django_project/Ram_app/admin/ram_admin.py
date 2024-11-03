from django.contrib import admin
from Ram_app.models import Ram_main


@admin.register(Ram_main)
class RamAdmin(admin.ModelAdmin):
    list_display = ('ram_name', 'ram_manufacturer', 'ram_form_factor', 'ram_size', 'ram_amount', 'ram_description')
