from django.db.models.query import QuerySet
from spares_tracker.vehicles.models import Vehicle
from spares_tracker.vehicles.filters import BaseVehicleFilter


def vehicle_list(*, filters=None) -> QuerySet[Vehicle]:
    filters = filters or {}

    qs = Vehicle.objects.all()
    return BaseVehicleFilter(filters, qs).qs
