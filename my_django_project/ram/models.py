from django.db import models
import uuid

class Ram(models.Model):
    id_ram = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    ram_size = models.CharField(max_length=50)
    ram_amount = models.CharField(max_length=50)
    description = models.TextField()

class RamRecomendedBuild(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_buildram