from django.urls import path

from .apis import VehicleCreateApi, VehicleListApi, VehicleUpdateApi


urlpatterns = [
    path('create/', VehicleCreateApi.as_view(), name='vehicle_create'),
    path('<int:vehicle_id>/update/', VehicleUpdateApi.as_view(), name='vehicle_update'),
    path('<int:vehicle_id>/delete/', VehicleUpdateApi.as_view(), name='vehicle_delete'),
    path('', VehicleListApi.as_view(), name='list')
]
