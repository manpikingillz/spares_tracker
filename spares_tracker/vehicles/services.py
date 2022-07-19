from spares_tracker.vehicles.models import Vehicle
from django.core.exceptions import ValidationError
from django.db import transaction
from spares_tracker.common.services import model_update
from collections import OrderedDict



MANUFACTURE_YEAR_GREATER_THAN_REGISTRATION_YEAR = 'Manufacture year cannot be greater than registration year'
MANUFACTURE_MONTH_GREATER_THAN_REGISTRATION_YEAR_IN_SAME_YEAR = '''
Manufacture Month can not be greater than registration month in the same year.
'''
VEHICLE_INSTANCE_IS_NONE='You attempted updating a vehicle that does not exist!'
VEHICLE_INSTANCE_IS_NONE_DELETE='You attempted deleting a vehicle that does not exist!'

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


@transaction.atomic
def vehicle_update(*, vehicle: Vehicle, data) -> Vehicle:
    non_side_effect_fields = [
        'number_plate',
        'country_of_registration',
        'chasis_number',
        'registration_year',
        'registration_month',
        'manufacture_year',
        'manufacture_month',
        'vehicle_model',
        'vehicle_model_code',
        'engine_size',
        'exterior_color',
        'fuel',
        'transmission',
        'body_type',
        'drive_train',
        'steering',
        'removed'
    ]

    if not vehicle:
        raise ValidationError(VEHICLE_INSTANCE_IS_NONE)

    _vehicle, has_updated = model_update(
        instance=vehicle,
        fields=non_side_effect_fields,
        data=data
    )
    print(f'vehicle::: {_vehicle}')

    return _vehicle


@transaction.atomic
def vehicle_delete(*, vehicle: Vehicle):
    if not vehicle:
        raise ValidationError(VEHICLE_INSTANCE_IS_NONE_DELETE)

    _dict_data = OrderedDict()
    _dict_data['removed'] = True
    vehicle_update(vehicle, data=_dict_data)