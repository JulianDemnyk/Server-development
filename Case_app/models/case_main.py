from django.db import models
import uuid


class CaseMain(models.Model):
    id_case = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    case_name = models.CharField(max_length=50)
    case_manufacturer = models.CharField(max_length=50)
    case_form_factor = models.CharField(max_length=50)
    case_fan_place = models.IntegerField()
    case_power_supply = models.CharField(max_length=50)
    case_description = models.TextField()
