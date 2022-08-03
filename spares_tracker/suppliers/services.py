

from spares_tracker.suppliers.models import Supplier


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