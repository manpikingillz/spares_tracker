from spares_tracker.vehicles.models import Vehicle
from django.core.exceptions import ValidationError


MANUFACTURE_YEAR_GREATER_THAN_REGISTRATION_YEAR = 'Manufacture year cannot be greater than registration year'
MANUFACTURE_MONTH_GREATER_THAN_REGISTRATION_YEAR_IN_SAME_YEAR = '''
Manufacture Month can not be greater than registration month in the same year.
'''

def vehicle_create(
    *,
    number_plate,
    country_of_registration,
    chasis_number,
    registration_year,
    registration_month,
    manufacture_year,
    manufacture_month,
    vehicle_model,
    vehicle_model_code,
    engine_size,
    exterior_color,
    fuel,
    transmission,
    body_type,
    drive_train,
    steering
) -> Vehicle:
    #TODO: Could extract all the validations to another method
    if manufacture_year > registration_year:
        raise ValidationError(
            MANUFACTURE_YEAR_GREATER_THAN_REGISTRATION_YEAR
        )

    if manufacture_year == registration_year & \
        manufacture_month > registration_month:
            raise ValidationError(
                MANUFACTURE_MONTH_GREATER_THAN_REGISTRATION_YEAR_IN_SAME_YEAR
            )

    vehicle = Vehicle(
        number_plate=number_plate,
        country_of_registration=country_of_registration,
        chasis_number=chasis_number,
        registration_year=registration_year,
        registration_month=registration_month,
        manufacture_year=manufacture_year,
        manufacture_month=manufacture_month,
        vehicle_model=vehicle_model,
        vehicle_model_code=vehicle_model_code,
        engine_size=engine_size,
        exterior_color=exterior_color,
        fuel=fuel,
        transmission=transmission,
        body_type=body_type,
        drive_train=drive_train,
        steering=steering
    )

    vehicle.full_clean()
    vehicle.save()

    return vehicle
