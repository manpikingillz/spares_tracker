from django.contrib import admin

from spares_tracker.employee.models import Division, Employee, Region, Section, Station


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'middle_name', 'gender', 'email', 'phone_number', 'address', 'station', 'section', 'user')


@admin.register(Station)
class StationAdmin(admin.ModelAdmin):
    list_display = ('name', 'division')


@admin.register(Division)
class DivisionAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_of_repair_process')