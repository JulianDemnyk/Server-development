from django.contrib import admin
from Ram_app.models import RamRecomendedBuild


@admin.register(RamRecomendedBuild)
class RamRecomendedBuildAdmin(admin.ModelAdmin):
    list_display = ('ram_id',)
