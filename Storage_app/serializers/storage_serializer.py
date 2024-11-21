from rest_framework import serializers
from Storage_app.models.storage_main import StorageMain


class StorageMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = StorageMain
        fields = [
            'id_storage',
            'storage_name',
            'storage_manufacturer',
            'storage_storage_type',
            'storage_capacity',
            'storage_description',
        ]
