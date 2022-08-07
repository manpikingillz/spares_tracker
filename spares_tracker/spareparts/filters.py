from dataclasses import fields
import django_filters

from spares_tracker.spareparts.models import SparePart, SparePartCategory

class BaseSparePartFilter(django_filters.FilterSet):
    class Meta:
        model = SparePart
        fields = ('name', 'code', 'category')


class BaseSparePartCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = SparePartCategory
        fields = ('category_name', 'relates_to')