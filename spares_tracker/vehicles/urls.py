from django.urls import path

from .apis import VehicleCreateApi


urlpatterns = [
    path('create/', VehicleCreateApi.as_view(), name='create')
]
