from django.contrib import admin
from Case_app.models.case_main import CaseMain


@admin.register(CaseMain)
class CaseMainAdmin(admin.ModelAdmin):
    list_display = ('case_name', 'case_manufacturer', 'case_form_factor', 'case_fan_place', 'case_power_supply', 'case_description')