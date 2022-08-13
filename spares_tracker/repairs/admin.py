from django.contrib import admin

from spares_tracker.repairs.models import Repair, RepairComment, RepairProblem, RepairProblemRecommendation, RepairSparePartRecommendation

@admin.register(Repair)
class RepairAdmin(admin.ModelAdmin):
    list_display = ('vehicle','problem_description', 'solution_description', 'status', 'section')

@admin.register(RepairProblem)
class RepairProblemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)

@admin.register(RepairComment)
class RepairCommentAdmin(admin.ModelAdmin):
    list_display = ('repair', 'comment', 'commented_by')

@admin.register(RepairProblemRecommendation)
class RepairProblemRecommendationAdmin(admin.ModelAdmin):
    list_display = ('repair', 'problem', 'added_by')

@admin.register(RepairSparePartRecommendation)
class RepairSparePartRecommendationAdmin(admin.ModelAdmin):
    list_display = ('repair', 'sparepart', 'added_by')