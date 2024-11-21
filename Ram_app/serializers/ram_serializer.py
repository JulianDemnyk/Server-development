from rest_framework import serializers
from Ram_app.models.ram_main import RamMain

class RamMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RamMain
        fields = [
            'id_ram',
            'ram_name',
            'ram_manufacturer',
            'ram_form_factor',
            'ram_size',
            'ram_amount',
            'ram_description',
        ]
