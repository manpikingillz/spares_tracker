from spares_tracker.common.utils import get_object
from django.db.models.query import QuerySet
from spares_tracker.vehicles.models import Vehicle, VehicleMake, VehicleModel
from spares_tracker.vehicles.filters import BaseVehicleFilter, BaseVehicleModelFilter


def vehicle_list(*, filters=None) -> QuerySet[Vehicle]:
    filters = filters or {}

    qs = Vehicle.objects.filter(removed=False)
    return BaseVehicleFilter(filters, qs).qs

def vehicle_detail(*, pk) -> Vehicle:
    return get_object(Vehicle, pk=pk)

def vehicle_make_list() -> QuerySet[VehicleMake]:
    return VehicleMake.objects.all()

def vehicle_model_list(*, filters=None) -> QuerySet[VehicleModel]:
    filters = filters or {}

    qs = VehicleModel.objects.all()
    return BaseVehicleModelFilter(filters, qs).qs
