from django.contrib import admin
from Recomendedbuild_app.models import RecommendedBuild_main


@admin.register(RecommendedBuild_main)
class RecomendedbuildAdmin(admin.ModelAdmin):
    list_display = ('id_build',)
