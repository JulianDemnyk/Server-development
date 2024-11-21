from rest_framework import serializers
from Powersupply_app.models.powersupply_main import PowerSupplyMain


class PowerSupplyMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerSupplyMain
        fields = [
            'id_powersupply',
            'powersupply_name',
            'powersupply_manufacturer',
            'powersupply_power',
            'powersupply_description',
        ]
