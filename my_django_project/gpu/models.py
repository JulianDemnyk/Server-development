from django.db import models
import uuid


class Gpu(models.Model):
    id_gpu = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    ram = models.CharField(max_length=50)
    ram_type = models.CharField(max_length=50)
    description = models.TextField()