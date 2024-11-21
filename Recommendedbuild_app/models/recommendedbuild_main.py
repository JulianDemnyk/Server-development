from django.db import models
import uuid


class RecommendedBuildMain(models.Model):
    id_build = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_cpubuild
    # id_gpubuild
    # id_motherboardbuild
    # id_rambuild
    # id_coolingsystembuild
    # id_powersupplybuild
    # id_casebuild
