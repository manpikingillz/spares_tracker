import django_filters

from spares_tracker.vehicles.models import Vehicle, VehicleModel


class BaseVehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ('number_plate', )

class BaseVehicleModelFilter(django_filters.FilterSet):
    class Meta:
        model = VehicleModel
        fields = ('vehicle_make', )