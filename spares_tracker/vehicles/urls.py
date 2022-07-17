from django.urls import path

from .apis import VehicleCreateApi


urlpatterns = [
    path('create/', VehicleCreateApi.as_view(), name='vehicle_create'),
    path('update/:vehicle_id', VehicleCreateApi.as_view(), name='vehicle_update')
]
