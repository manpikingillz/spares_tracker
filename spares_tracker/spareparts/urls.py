from django.urls import path

from .apis import (
    SparePartCategoryListApi,
    SparePartListApi,
    SparePartPurchaseCreateApi,
    SparePartPurchaseListApi,
    SparePartPurchaseDetailApi
)

urlpatterns = [
    path('', SparePartListApi.as_view(), name='sparepart_list'),
    path('categories/', SparePartCategoryListApi.as_view(), name='sparepart_category_list'),
    path('sparepart_purchases/create/', SparePartPurchaseCreateApi.as_view(), name='sparepart_purchases_create'),
    path('sparepart_purchases/', SparePartPurchaseListApi.as_view(), name='sparepart_purchases_list'),
    path('sparepart_purchases/<int:sparepart_purchase_id>/', SparePartPurchaseDetailApi.as_view(), name='sparepart_purchases_detail'),
]