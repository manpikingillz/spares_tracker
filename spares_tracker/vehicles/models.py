from django.db import models
from spares_tracker.common.models import BaseModel
from datetime import date
from django.db.models import Q

class Country(models.Model):
    country_name = models.CharField(max_length=255)

    def __str__(self):
        return self.country_name


class VehicleMake(models.Model):
    vehicle_make_name = models.CharField(max_length=255)

    def __str__(self):
        return self.vehicle_make_name

class VehicleModel(models.Model):
    vehicle_model_name = models.CharField(max_length=255)
    vehicle_make = models.ForeignKey(VehicleMake, related_name='vehicle_models', on_delete=models.CASCADE)

    def __str__(self):
        return self.vehicle_model_name


class Vehicle(BaseModel):
    country_of_registration = models.ForeignKey(Country, related_name='vehicles', on_delete=models.CASCADE)
    chasis_number = models.CharField(max_length=255)
    registration_year = models.SmallIntegerField()
    registration_month = models.SmallIntegerField()
    manufacture_year = models.SmallIntegerField()
    manufacture_month = models.SmallIntegerField()
    vehicle_model = models.ForeignKey(VehicleModel, related_name='vehicles', on_delete=models.CASCADE)
    vehicle_model_code = models.CharField(max_length=255)
    engine_size = models.SmallIntegerField()
    exterior_color = models.CharField(max_length=10)
    fuel = models.CharField(max_length=10)
    transmission = models.CharField(max_length=50)
    body_type = models.CharField(max_length=50)

    def __str__(self):
        return f'''{self.manufacture_year}
                    {self.vehicle_model.vehicle_make.vehicle_make_name}
                    {self.vehicle_model.vehicle_model_name}
                    {self.vehicle_model_code}
                    '''
    class Meta:
        constraints = [
            models.CheckConstraint(
                name='registration_year_between_1980_and_current_year',
                check=Q(registration_year__gte=1980) & Q(registration_year__lte=date.today().year)
            ),
            models.CheckConstraint(
                name='registration_month_between_1_and_12',
                check=Q(registration_month__gte=1) & Q(registration_month__lte=12)
            ),
            models.CheckConstraint(
                name='manufacture_year_between_1980_and_current_year',
                check=Q(manufacture_year__gte=1980) & Q(manufacture_year__lte=date.today().year)
            ),
            models.CheckConstraint(
                name='manufacture_month_between_1_and_12',
                check=Q(manufacture_month__gte=1) & Q(manufacture_month__lte=12)
            ),
        ]