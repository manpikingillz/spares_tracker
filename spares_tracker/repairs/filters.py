import django_filters
from spares_tracker.repairs.models import Repair, RepairProblem


class BaseRepairFilter(django_filters.FilterSet):
    class Meta:
        model = Repair
        fields = ('vehicle', )


class BaseRepairProblemFilter(django_filters.FilterSet):
    class Meta:
        model = RepairProblem
        fields = ('name', )

