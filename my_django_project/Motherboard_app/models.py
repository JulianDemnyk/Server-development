from django.db import models
import uuid


class Motherboard_main(models.Model):
    id_motherboard = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    motherboard_name = models.CharField(max_length=50)
    motherboard_manufacturer = models.CharField(max_length=50)
    motherboard_socket_motherboard = models.CharField(max_length=50)
    motherboard_ram_type = models.CharField(max_length=50)
    motherboard_sata_slot = models.IntegerField()
    motherboard_m2_slot = models.IntegerField()
    motherboard_form_factor = models.CharField(max_length=50)
    motherboard_description = models.TextField()
