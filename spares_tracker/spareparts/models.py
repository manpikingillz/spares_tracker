from django.db import models

from spares_tracker.common.models import BaseModel
from spares_tracker.files.models import File

# Create your models here.
class SparePartsCategory(BaseModel):
    category_name = models.CharField(max_length=255, unique=True)
    image = models.ForeignKey(
        File,
        related_name='sparepart_category_images',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    relates_to = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.category_name