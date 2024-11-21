from rest_framework import serializers
from Motherboard_app.models.motherboard_main import MotherboardMain


class MotherboardMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherboardMain
        fields = [
            'id_motherboard',
            'motherboard_name',
            'motherboard_manufacturer',
            'motherboard_socket_motherboard',
            'motherboard_ram_type',
            'motherboard_sata_slot',
            'motherboard_m2_slot',
            'motherboard_form_factor',
            'motherboard_description',
        ]
