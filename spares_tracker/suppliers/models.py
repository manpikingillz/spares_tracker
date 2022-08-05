from django.db import models
from spares_tracker.common.models import BaseModel

class Supplier(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone = models.CharField(max_length=30)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name