import django_filters

from spares_tracker.spareparts.models import SparePart

class BaseSparePartFilter(django_filters.FilterSet):
    class Meta:
        model = SparePart
        fileds = ('name', 'code',)