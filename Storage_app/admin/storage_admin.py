from django.contrib import admin
from Storage_app.models.storage_main import StorageMain


@admin.register(StorageMain)
class StorageAdmin(admin.ModelAdmin):
    list_display = ('id_storage', 'storage_name', 'storage_manufacturer', 'storage_storage_type', 'storage_capacity')
    search_fields = ('storage_name', 'storage_manufacturer')
