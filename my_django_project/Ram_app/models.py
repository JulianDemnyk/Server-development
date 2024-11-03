from django.db import models
import uuid


class Ram_main(models.Model):
    id_ram = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ram_name = models.CharField(max_length=50)
    ram_manufacturer = models.CharField(max_length=50)
    ram_form_factor = models.CharField(max_length=50)
    ram_size = models.CharField(max_length=50)
    ram_amount = models.CharField(max_length=50)
    ram_description = models.TextField()


class RamRecomendedBuild(models.Model):
    ram_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_buildram