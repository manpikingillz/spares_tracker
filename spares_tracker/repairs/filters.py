import django_filters
from spares_tracker.repairs.models import Repair


class BaseRepairFilter(django_filters.FilterSet):
    class Meta:
        model = Repair
        fields = ('vehicle', )

