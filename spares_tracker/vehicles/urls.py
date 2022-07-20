from django.urls import path

from .apis import (
    VehicleCreateApi,
    VehicleListApi,
    VehicleUpdateApi,
    VehicleDeleteApi,
    VehicleMakeApi,
    VehicleModelApi
)


urlpatterns = [
    path('create/', VehicleCreateApi.as_view(), name='vehicle_create'),
    path('<int:vehicle_id>/update/', VehicleUpdateApi.as_view(), name='vehicle_update'),
    path('<int:vehicle_id>/delete/', VehicleDeleteApi.as_view(), name='vehicle_delete'),
    path('', VehicleListApi.as_view(), name='vehicle_list'),
    path('vehicle_makes/', VehicleMakeApi.as_view(), name='vehicle_make_list'),
    path('vehicle_models/', VehicleModelApi.as_view(), name='vehicle_model_list'),
]
