from django.db import models

from spares_tracker.common.models import BaseModel
from spares_tracker.files.models import File
from spares_tracker.employee.models import Employee
from spares_tracker.vehicles.models import VehicleModel
from spares_tracker.suppliers.models import Supplier

# Create your models here.
class SparePartCategory(BaseModel):
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


class SparePart(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ForeignKey(
        File,
        related_name='spare_parts',
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    barcode = models.ForeignKey(
        File,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        'SparePartCategory',
        related_name='spare_parts',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    vehicle_models=models.ManyToManyField(
        VehicleModel,
        related_name='spare_parts',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.name} {self.code}'


class SparePartPurchase(BaseModel):
    spare_part = models.ForeignKey(
        'SparePart',
        related_name='spare_part_purchases',
        on_delete=models.CASCADE
    )
    order_number = models.CharField(max_length=255, blank=True, null=True)
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=15, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=15, decimal_places=2)
    supplied_by = models.ForeignKey(
        Supplier,
        related_name='spare_part_purchases',
        on_delete=models.CASCADE
    )
    received_by = models.ForeignKey(
        Employee,
        related_name='spare_part_purchases',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f'{self.spare_part.name} - {self.quantity}'