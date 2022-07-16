from django.contrib import admin
from spares_tracker.vehicles.models import Vehicle
# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('country_of_registration', 'chasis_number', 'registration_year', 'registration_month',
                    'manufacture_year', 'manufacture_month', 'vehicle_model', 'vehicle_model_code', 'engine_size',
                    'exterior_color', 'fuel', 'transmission', 'body_type')