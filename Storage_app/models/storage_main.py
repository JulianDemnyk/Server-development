from django.db import models
import uuid


class StorageMain(models.Model):
    id_storage = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    storage_name = models.CharField(max_length=50)
    storage_manufacturer = models.CharField(max_length=50)
    storage_storage_type = models.CharField(max_length=50)
    storage_capacity = models.IntegerField()
    storage_description = models.TextField()