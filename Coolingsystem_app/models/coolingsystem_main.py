from django.db import models
import uuid


class CoolingSystemMain(models.Model):
    id_coolingsystem = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coolingsystem_name = models.CharField(max_length=50)
    coolingsystem_manufacturer = models.CharField(max_length=50)
    coolingsystem_form_factor = models.IntegerField()
    coolingsystem_tdp = models.IntegerField()
    coolingsystem_description = models.TextField()
