from django.contrib import admin
from spares_tracker.spareparts.models import SparePart, SparePartCategory, SparePartPurchase


@admin.register(SparePartCategory)
class SparePartCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','image', 'relates_to')


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('name', 'code','quantity', 'price', 'image', 'barcode', 'category')

@admin.register(SparePartPurchase)
class SparePartPurchase(admin.ModelAdmin):
    list_display = ('spare_part', 'order_number', 'quantity', 'unit_price', 'amount_paid', 'supplied_by', 'received_by',)
