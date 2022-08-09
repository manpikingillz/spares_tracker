from django.db import models

from spares_tracker.common.models import BaseModel
from spares_tracker.spareparts.models import SparePart
from spares_tracker.vehicles.models import Vehicle

# Create your models here.
class Repair(BaseModel):
    vehicle = models.ForeignKey(
        Vehicle,
        related_name='repairs',
        on_delete=models.CASCADE
    )
    problem_description = models.TextField()
    solution_description = models.TextField()
    spare_parts = models.ManyToManyField(
        SparePart,
        related_name='repairs',
        null=True,
        blank=True
    )
    problems = models.ManyToManyField(
        'RepairProblem',
        related_name='repairs',
        null=True,
        blank=True
    )

    def __str__(self):
        return f'{self.vehicle.number_plate} - {self.problem_description}'

class RepairProblem(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __Str__(self):
        return self.name