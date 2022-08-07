from django.urls import path

from .apis import (
    SparePartCategoryListApi,
)

urlpatterns = [
    path('', SparePartCategoryListApi.as_view(), name='sparepart_category_list'),
]