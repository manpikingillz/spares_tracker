import django_filters
from spares_tracker.repairs.models import Repair, RepairProblem, RepairProblemRecommendation, RepairSparePartRecommendation


class BaseRepairFilter(django_filters.FilterSet):
    class Meta:
        model = Repair
        fields = ('vehicle', )


class BaseRepairProblemFilter(django_filters.FilterSet):
    class Meta:
        model = RepairProblem
        fields = ('name', )

class BaseRepairProblemRecommendationFilter(django_filters.FilterSet):
    class Meta:
        model = RepairProblemRecommendation
        fields = ('repair', 'problem', 'added_by')
        
class BaseRepairSparePartRecommendationFilter(django_filters.FilterSet):
    class Meta:
        model = RepairSparePartRecommendation
        fields = ('repair', 'sparepart', 'added_by')
