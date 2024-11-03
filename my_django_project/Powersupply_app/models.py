from django.db import models
import uuid


class PowerSupply_main(models.Model):
    id_powersupply = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    powersupply_name = models.CharField(max_length=50)
    powersupply_manufacturer = models.CharField(max_length=50)
    powersupply_power = models.IntegerField()
    powersupply_description = models.TextField()
