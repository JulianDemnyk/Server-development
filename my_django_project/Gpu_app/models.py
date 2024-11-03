from django.db import models
import uuid


class Gpu_main(models.Model):
    id_gpu = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    gpu_name = models.CharField(max_length=50)
    gpu_manufacturer = models.CharField(max_length=50)
    gpu_series = models.CharField(max_length=50)
    gpu_ram = models.CharField(max_length=50)
    gpu_ram_type = models.CharField(max_length=50)
    gpu_description = models.TextField()