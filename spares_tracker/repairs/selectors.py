from django.db.models.query import QuerySet
from spares_tracker.repairs.models import Repair, RepairProblem
from spares_tracker.repairs.filters import BaseRepairFilter

#  Repair selectors
def repair_list(*, filters=None) -> QuerySet[Repair]:
    filters = filters or {}

    qs = Repair.objects.filter(removed=False)
    return BaseRepairFilter(filters, qs).qs


def repair_problem_list(*, filters=None) -> QuerySet[RepairProblem]:
    filters = filters or {}

    qs = RepairProblem.objects.filter(removed=False)
    return BaseRepairFilter(filters, qs).qs

