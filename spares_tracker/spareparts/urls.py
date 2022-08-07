from django.urls import path

from .apis import (
    SparePartCategoryListApi,
    SparePartListApi
)

urlpatterns = [
    path('', SparePartListApi.as_view(), name='sparepart_list'),
    path('categories/', SparePartCategoryListApi.as_view(), name='sparepart_category_list'),
]