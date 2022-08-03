from django.urls import path

from .apis import (
    SupplierCreateApi,
    SupplierListApi
)

urlpatterns = [
    path('create/', SupplierCreateApi.as_view(), name='supplier_create'),
    path('', SupplierListApi.as_view(), name='supplier_list'),
]