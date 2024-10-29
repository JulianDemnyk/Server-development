from django.db import models
import uuid

class Storage(models.Model):
    id_storage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    manufacturer = models.CharField(max_length=50)
    storage_type = models.CharField(max_length=50)
    capacity = models.IntegerField(max_length=50)
    description = models.TextField()

class StorageRecomendedBuild(models.Model):
    id_storage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # id_buildstorage