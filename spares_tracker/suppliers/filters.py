import django_filters

from spares_tracker.suppliers.models import Supplier

class BaseSupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fileds = ('name', 'email', 'phone')