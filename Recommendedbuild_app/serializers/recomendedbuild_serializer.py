from rest_framework import serializers
from Recommendedbuild_app.models.recommendedbuild_main import RecommendedBuildMain


class RecommendedBuildMainSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecommendedBuildMain
        fields = [
            'id_build',
            # Add the related fields (id_cpubuild, id_gpubuild, etc.) once the relationships are defined
        ]
