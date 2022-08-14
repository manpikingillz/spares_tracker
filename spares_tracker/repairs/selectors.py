from django.db.models.query import QuerySet
from spares_tracker.repairs.models import Repair, RepairComment, RepairProblem, RepairSparePartRecommendation
from spares_tracker.repairs.filters import BaseRepairCommentFilter, BaseRepairFilter, BaseRepairProblemRecommendationFilter, BaseRepairSparePartRecommendationFilter
from spares_tracker.common.utils import get_object
from spares_tracker.repairs.models import RepairProblemRecommendation

#  Repair selectors
def repair_list(*, filters=None) -> QuerySet[Repair]:
    filters = filters or {}

    qs = Repair.objects.filter(removed=False)
    return BaseRepairFilter(filters, qs).qs


def repair_detail(*, pk) -> Repair:
    return get_object(Repair, pk=pk)


def repair_problem_list(*, filters=None) -> QuerySet[RepairProblem]:
    filters = filters or {}

    qs = RepairProblem.objects.filter(removed=False)
    return BaseRepairFilter(filters, qs).qs


def repair_problem_recommendation_list(*, filters=None) -> QuerySet[RepairProblemRecommendation]:
    filters = filters or {}

    qs = RepairProblemRecommendation.objects.filter(removed=False)
    return BaseRepairProblemRecommendationFilter(filters, qs).qs


def repair_sparepart_recommendation_list(*, filters=None) -> QuerySet[RepairSparePartRecommendation]:
    filters = filters or {}

    qs = RepairSparePartRecommendation.objects.filter(removed=False)
    return BaseRepairSparePartRecommendationFilter(filters, qs).qs

def repair_comment_list(*, filters=None) -> QuerySet[RepairComment]:
    filters = filters or {}

    qs = RepairComment.objects.filter(removed=False)
    return BaseRepairCommentFilter(filters, qs).qs