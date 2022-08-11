from django.contrib import admin

from spares_tracker.repairs.models import Repair, RepairComment, RepairProblem

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('vehicle','problem_description', 'solution_description', 'status', 'section')

@admin.register(RepairProblem)
class RepairProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

@admin.register(RepairComment)
class RepairCommentAdmin(admin.ModelAdmin):
    list_display = ('repair', 'employee', 'comment')