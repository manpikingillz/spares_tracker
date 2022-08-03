from django.urls import path

from .apis import (
    SupplierCreateApi,
    SupplierListApi,
    SupplierUpdateApi
)

urlpatterns = [
    path('create/', SupplierCreateApi.as_view(), name='supplier_create'),
    path('', SupplierListApi.as_view(), name='supplier_list'),
    path('<int:supplier_id>/update/', SupplierUpdateApi.as_view(), name='supplier_update'),
]