from django.db import models
import uuid


class Motherboard(models.Model):
    id_motherboard = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    socket_motherboard = models.CharField(max_length=50)
    ram_type = models.CharField(max_length=50)
    sata_slot = models.IntegerField(max_length=1)
    m2_slot = models.IntegerField(max_length=1)
    form_factor = models.CharField(max_length=50)
    description = models.TextField()
