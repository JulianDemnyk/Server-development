from django.db import models
import uuid


class PowerSupply(models.Model):
    id_powersupply = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    power = models.DecimalField(max_digits=50)
    description = models.TextField()
