from spares_tracker.suppliers.models import Supplier
from django.db.models.query import QuerySet
from spares_tracker.vehicles.filters import BaseVehicleFilter


def supplier_list(*, filters=None) -> QuerySet[Supplier]:
    filters = filters or {}

    qs = Supplier.objects.filter(removed=False)
    return BaseVehicleFilter(filters, qs).qs