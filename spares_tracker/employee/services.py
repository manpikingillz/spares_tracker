from django.db import transaction
from spares_tracker.employee.models import Employee
from django.core.exceptions import ValidationError
from spares_tracker.common.services import model_update, model_delete

EMPLOYEE_INSTANCE_IS_NONE = f'You attempted updating a {Employee.__name__} that does not exist!'
EMPLOYEE_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {Employee.__name__} that does not exist!'

def employee_create(
    *,
    first_name,
    last_name,
    middle_name,
    gender,
    email,
    phone_number,
    address,
    station,
    section
) -> Employee:
    employee = Employee(
        first_name=first_name,
        last_name=last_name,
        middle_name=middle_name,
        gender=gender,
        email=email,
        phone_number=phone_number,
        address=address,
        station=station,
        section=section
    )

    employee.full_clean()
    employee.save()

    return employee


@transaction.atomic
def employee_update(*, employee: Employee, data) -> Employee:
    model_fields = list(vars(employee).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not employee:
        raise ValidationError(EMPLOYEE_INSTANCE_IS_NONE)

    _employee, has_updated = model_update(
        instance=employee,
        fields=model_fields,
        data=data
    )

    return _employee


@transaction.atomic
def employee_delete(*, employee: Employee):

    if not employee:
        raise ValidationError(EMPLOYEE_INSTANCE_IS_NONE_DELETE)

    model_delete(instance=employee)