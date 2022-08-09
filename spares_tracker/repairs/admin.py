from django.contrib import admin

from spares_tracker.repairs.models import Repair, RepairProblem

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('vehicle','problem_description', 'solution_description')

@admin.register(RepairProblem)
class RepairProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)