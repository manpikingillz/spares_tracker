import django_filters

from spares_tracker.vehicles.models import Vehicle


class BaseVehicleFilter(django_filters.FilterSet):
    class Meta:
        model = Vehicle
        fields = ('number_plate', )