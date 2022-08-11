from tkinter import CASCADE
from django.db import models

from spares_tracker.common.models import BaseModel
from spares_tracker.spareparts.models import SparePart
from spares_tracker.employee.models import Employee, Section
from spares_tracker.users.models import BaseUser
from spares_tracker.vehicles.models import Vehicle


class RepairProblemRecommendation(BaseModel):
    repair = models.ForeignKey(
        'Repair',
        related_name='repair_problem_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    problem = models.ForeignKey(
        'RepairProblem',
        related_name='repair_problem_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    added_by = models.ForeignKey(
        BaseUser,
        related_name='repair_problem_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class RepairSparePartRecommendation(BaseModel):
    repair = models.ForeignKey(
        'Repair',
        related_name='repair_sparepart_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    sparepart = models.ForeignKey(
        SparePart,
        related_name='repair_sparepart_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    added_by = models.ForeignKey(
        BaseUser,
        related_name='repair_sparepart_recommendations',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

class Repair(BaseModel):
    class Status(models.TextChoices):
        RECEIVED = 'RECEIVED', 'Received'
        FOR_REVIEW = 'FOR_REVIEW', 'For Review'
        FOR_DIRECTOR_APPROVAL = 'FOR_DIRECTOR_APPROVAL', 'For Director Approval'
        FOR_REPAIR = 'FOR_REPAIR', 'For Repair'
        FOR_PICKING = 'FOR_PICKING', 'For Picking'

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
        through='RepairSparePartRecommendation',
        null=True,
        blank=True
    )
    problems = models.ManyToManyField(
        'RepairProblem',
        through='RepairProblemRecommendation',
        related_name='repairs',
        null=True,
        blank=True
    )
    status = models.CharField(
        choices=Status.choices,
        max_length=255,
        default=Status.RECEIVED,
        null=True, blank=True
    )
    section = models.ForeignKey(
        Section,
        related_name='repairs',
        on_delete=models.CASCADE,
        null=True, blank=True
    )
    added_by = models.ForeignKey(
        BaseUser,
        related_name='repairs',
        on_delete=models.CASCADE,
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


class RepairComment(BaseModel):
    repair = models.ForeignKey(Repair, related_name='repair_comments', on_delete=models.CASCADE, null=True, blank=True),
    employee = models.ForeignKey(Employee, related_name='repair_comments', on_delete=models.CASCADE, null=True, blank=True),
    comment = models.TextField()
