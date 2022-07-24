from django.contrib import admin
from spares_tracker.setup.models import Country


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ('country_name',)
