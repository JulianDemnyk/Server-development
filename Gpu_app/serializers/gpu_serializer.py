from rest_framework import serializers
from Gpu_app.models.gpu_main import GpuMain


class GpuMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = GpuMain
        fields = [
            'id_gpu',
            'gpu_name',
            'gpu_manufacturer',
            'gpu_series',
            'gpu_ram',
            'gpu_ram_type',
            'gpu_description',
        ]
