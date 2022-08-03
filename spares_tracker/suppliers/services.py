from django.db import transaction
from spares_tracker.suppliers.models import Supplier
from django.core.exceptions import ValidationError
from spares_tracker.common.services import model_update

SUPPLIER_INSTANCE_IS_NONE = f'You attempted updating a {Supplier.__name__} that does not exist!'

def supplier_create(
    *,
    name,
    email,
    phone,
    address
) -> Supplier:
    supplier = Supplier(
        name=name,
        email=email,
        phone=phone,
        address=address
    )

    supplier.full_clean()
    supplier.save()

    return supplier


@transaction.atomic
def supplier_update(*, supplier: Supplier, data) -> Supplier:
    model_fields = list(vars(supplier).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not supplier:
        raise ValidationError(SUPPLIER_INSTANCE_IS_NONE)

    _supplier, has_updated = model_update(
        instance=supplier,
        fields=model_fields,
        data=data
    )

    return _supplier
