from django.db import models
import uuid


class Case(models.Model):
    id_case = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    form_factor = models.CharField(max_length=50)
    fan_place = models.IntegerField(max_length=1)
    power_supply = models.CharField(max_length=50)
    description = models.TextField()
