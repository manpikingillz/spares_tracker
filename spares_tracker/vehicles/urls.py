from django.urls import path

from .apis import VehicleCreateApi, VehicleListApi


urlpatterns = [
    path('create/', VehicleCreateApi.as_view(), name='create'),
    path('', VehicleListApi.as_view(), name='list')
]
