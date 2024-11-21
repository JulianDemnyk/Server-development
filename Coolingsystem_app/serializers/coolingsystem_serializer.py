from rest_framework import serializers
from Coolingsystem_app.models.coolingsystem_main import CoolingSystemMain


class CoolingSystemMainSerializer(serializers.ModelSerializer):
    class Meta:
        models = CoolingSystemMain
        fields = [
            'id_coolingsystem',
            'coolingsystem_name',
            'coolingsystem_manufacturer',
            'coolingsystem_form_factor',
            'coolingsystem_tdp',
            'coolingsystem_description',
        ]
