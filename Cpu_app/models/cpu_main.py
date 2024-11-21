from django.db import models
import uuid


class CpuMain(models.Model):
    id_cpu = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cpu_name = models.CharField(max_length=50)
    cpu_manufacturer = models.CharField(max_length=50)
    cpu_series = models.CharField(max_length=50)
    cpu_socket = models.CharField(max_length=50)
    cpu_cores = models.IntegerField()
    cpu_threads = models.IntegerField()
    cpu_tdp = models.IntegerField()
    cpu_description = models.TextField()