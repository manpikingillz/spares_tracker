from django.urls import path

from .apis import (
    SupplierCreateApi
)

urlpatterns = [
    path('create/', SupplierCreateApi.as_view(), name='supplier_create')
]