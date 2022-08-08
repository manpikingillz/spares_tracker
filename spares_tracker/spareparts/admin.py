from django.contrib import admin
from spares_tracker.spareparts.models import SparePart, SparePartCategory


@admin.register(SparePartCategory)
class SparePartCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name','image', 'relates_to')


@admin.register(SparePart)
class SparePartAdmin(admin.ModelAdmin):
    list_display = ('name', 'code','quantity', 'price', 'image', 'barcode', 'category')
