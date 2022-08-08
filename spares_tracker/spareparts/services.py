from django.db import transaction
from spares_tracker.spareparts.models import SparePartCategory, SparePart
from django.core.exceptions import ValidationError
from spares_tracker.common.services import model_update, model_delete

SPAREPART_INSTANCE_IS_NONE = f'You attempted updating a {SparePart.__name__} that does not exist!'
SPAREPART_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {SparePart.__name__} that does not exist!'
SPAREPARTCATEGORY_INSTANCE_IS_NONE = f'You attempted updating a {SparePartCategory.__name__} that does not exist!'
SPAREPARTCATEGORY_INSTANCE_IS_NONE_DELETE = f'You attempted deleting a {SparePartCategory.__name__} that does not exist!'


def sparepart_create(
    *,
    name,
    code,
    category,
    vehicle_models
) -> SparePart:
    sparepart = SparePart(
        name=name,
        code=code,
        category=category
    )

    sparepart.full_clean()
    sparepart.save()
    # sparepart.vehicle_models.add(vehicle_models)

    return sparepart


@transaction.atomic
def sparepart_update(*, sparepart: SparePart, data) -> SparePart:
    model_fields = list(vars(sparepart).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not sparepart:
        raise ValidationError(SPAREPART_INSTANCE_IS_NONE)

    _sparepart, has_updated = model_update(
        instance=sparepart,
        fields=model_fields,
        data=data
    )

    return _sparepart


@transaction.atomic
def sparepart_delete(*, sparepart: SparePart):

    if not sparepart:
        raise ValidationError(SPAREPART_INSTANCE_IS_NONE_DELETE)

    model_delete(instance=sparepart)