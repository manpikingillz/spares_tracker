from dataclasses import fields
import django_filters

from spares_tracker.spareparts.models import SparePart, SparePartCategory, SparePartPurchase

class BaseSparePartFilter(django_filters.FilterSet):
    class Meta:
        model = SparePart
        fields = ('name', 'code', 'category', 'vehicle_models')


class BaseSparePartCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = SparePartCategory
        fields = ('category_name', 'relates_to')

class BaseSparePartPurchaseFilter(django_filters.FilterSet):
    class Meta:
        model = SparePartPurchase
        fields = ('spare_part', 'order_number')
