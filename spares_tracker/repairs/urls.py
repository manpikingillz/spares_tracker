from django.urls import path

from .apis import (
    RepairListApi,
    RepairCreateApi
)

urlpatterns = [
    path('', RepairListApi.as_view(), name='repair_list'),
    path('create/', RepairCreateApi.as_view(), name='repair_create'),
]