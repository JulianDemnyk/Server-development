from django.contrib import admin
from Recommendedbuild_app.models.recommendedbuild_main import RecommendedBuildMain


@admin.register(RecommendedBuildMain)
class RecomendedBuildMainAdmin(admin.ModelAdmin):
    list_display = ('id_build',)
