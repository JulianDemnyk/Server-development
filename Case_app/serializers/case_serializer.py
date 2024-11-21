from rest_framework import serializers
from Case_app.models.case_main import CaseMain


class CaseMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CaseMain
        fields = ['id_case',
                  'case_name',
                  'case_manufacturer',
                  'case_form_factor',
                  'case_fan_place',
                  'case_power_supply',
                  'case_description', ]
