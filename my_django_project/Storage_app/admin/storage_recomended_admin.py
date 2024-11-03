from django.contrib import admin
from Storage_app.models import StorageRecomendedBuild

@admin.register(StorageRecomendedBuild)
class StorageRecomendedBuildAdmin(admin.ModelAdmin):
    list_display = ('storage_id', )