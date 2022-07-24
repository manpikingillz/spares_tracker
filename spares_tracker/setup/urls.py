from django.urls import path

from .apis import (
    CountryListApi
)


urlpatterns = [
    path('countries/', CountryListApi.as_view(), name='country_list')
]
