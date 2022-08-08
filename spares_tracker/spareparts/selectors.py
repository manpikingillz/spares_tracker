from spares_tracker.common.utils import get_object
from spares_tracker.spareparts.models import SparePart, SparePartCategory, SparePartPurchase
from django.db.models.query import QuerySet
from spares_tracker.spareparts.filters import BaseSparePartFilter, BaseSparePartCategoryFilter, BaseSparePartPurchaseFilter

# spare parts selectors
def sparepart_list(*, filters=None) -> QuerySet[SparePart]:
    filters = filters or {}

    qs = SparePart.objects.filter(removed=False)
    return BaseSparePartFilter(filters, qs).qs


def sparepart_detail(*, pk) -> SparePart:
    return get_object(SparePart, pk=pk)



# spare parts category selectors
def sparepart_category_list(*, filters=None) -> QuerySet[SparePartCategory]:
    filters = filters or {}

    if filters.get('relates_to') is None:
        qs = SparePartCategory.objects.filter(removed=False, relates_to__isnull=True)
    else:
        qs = SparePartCategory.objects.filter(removed=False)
    return BaseSparePartCategoryFilter(filters, qs).qs

# spare parts purchases selectors
def sparepart_purchase_list(*, filters=None) -> QuerySet[SparePartPurchase]:
    filters = filters or {}

    qs = SparePartPurchase.objects.filter(removed=False)
    return BaseSparePartPurchaseFilter(filters, qs).qs


def sparepart_purchase_detail(*, pk) -> SparePartPurchase:
    return get_object(SparePartPurchase, pk=pk)