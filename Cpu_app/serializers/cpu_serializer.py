from rest_framework import serializers
from Cpu_app.models.cpu_main import CpuMain


class CpuMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = CpuMain
        fields = [
            'id_cpu',
            'cpu_name',
            'cpu_manufacturer',
            'cpu_series',
            'cpu_socket',
            'cpu_cores',
            'cpu_threads',
            'cpu_tdp',
            'cpu_description',
        ]
