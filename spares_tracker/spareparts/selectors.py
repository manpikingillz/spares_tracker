from spares_tracker.common.utils import get_object
from spares_tracker.spareparts.models import SparePart
from django.db.models.query import QuerySet
from spares_tracker.spareparts.filters import BaseSparePartFilter


def sparepart_list(*, filters=None) -> QuerySet[SparePart]:
    filters = filters or {}

    qs = SparePart.objects.filter(removed=False)
    return BaseSparePartFilter(filters, qs).qs


def sparepart_detail(*, pk) -> SparePart:
    return get_object(SparePart, pk=pk)