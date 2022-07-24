from django.contrib import admin
from spares_tracker.vehicles.models import (
    Vehicle, VehicleMake, VehicleModel)
# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('number_plate', 'country_of_registration', 'chasis_number', 'registration_year', 'registration_month',
                    'manufacture_year', 'manufacture_month', 'vehicle_model', 'vehicle_model_code', 'engine_size',
                    'exterior_color', 'fuel', 'transmission', 'body_type', 'drive_train', 'steering')

@admin.register(VehicleMake)
class VehicleMakeAdmin(admin.ModelAdmin):
    list_display = ('vehicle_make_name',)

@admin.register(VehicleModel)
class VehicleModelAdmin(admin.ModelAdmin):
    list_display = ('vehicle_model_name',)