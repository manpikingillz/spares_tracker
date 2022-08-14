from django.db import models

from spares_tracker.common.models import BaseModel
from spares_tracker.users.models import BaseUser


class Region(BaseModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.name


class Division(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    region = models.ForeignKey(Region, related_name='divisions', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Station(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    division = models.ForeignKey(Division, related_name='stations', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Section(BaseModel):
    name = models.CharField(max_length=255, unique=True)
    start_of_repair_process = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name


class Employee(BaseModel):
    class Gender(models.TextChoices):
        FEMALE = 'FEMALE', 'Female'
        MALE = 'MALE', 'Male'

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    middle_name = models.CharField(max_length=255, null=True, blank=True)
    gender =  models.CharField(choices=Gender.choices, max_length=6)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=30, unique=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    station =  models.ForeignKey(Station, related_name='employees', on_delete=models.CASCADE)
    section = models.ForeignKey(Section, related_name='employees', on_delete=models.CASCADE, null=True, blank=True)
    user = models.OneToOneField(BaseUser, related_name='employee', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.middle_name or " "} {self.last_name}'

    @property
    def full_name(self) -> str:
        return f'{self.first_name} {self.middle_name or ""} {self.last_name}'