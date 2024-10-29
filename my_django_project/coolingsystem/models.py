from django.db import models
import uuid


class CoolingSystem(models.Model):
    id_coolingsystem = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    form_factor = models.IntegerField(max_length=50)
    tdp = models.IntegerField(max_length=50)
    description = models.TextField()
