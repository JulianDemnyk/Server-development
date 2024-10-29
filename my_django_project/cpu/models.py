from django.db import models
import uuid


class Cpu(models.Model):
    id_cpu = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    socket_cpu = models.CharField(max_length=50)
    cores = models.IntegerField(max_length=2)
    threads = models.IntegerField(max_length=2)
    tdp = models.IntegerField(max_length=3)
    description = models.TextField()