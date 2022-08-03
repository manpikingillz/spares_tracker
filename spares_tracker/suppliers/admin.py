from django.contrib import admin
from spares_tracker.suppliers.models import Supplier

@admin.register(Supplier)
class VehicleAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
