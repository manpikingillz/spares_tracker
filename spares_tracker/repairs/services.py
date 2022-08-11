from django.db import transaction
from spares_tracker.repairs.models import Repair, RepairProblem, RepairProblemRecommendation, RepairSparePartRecommendation
from spares_tracker.common.utils import get_object
from spares_tracker.spareparts.models import SparePart


#  Repair services.
@transaction.atomic
def repair_create(
    *,
    vehicle,
    problem_description,
    solution_description,
    spare_parts=None,
    problems=None,
    user=None
) -> Repair:
    repair = Repair(
        vehicle=vehicle,
        problem_description=problem_description,
        solution_description=solution_description,
    )

    repair.full_clean()
    repair.save()

    created_repair = get_object(Repair, pk=repair.id)

    repair_spare_part_recommendation_create(spare_parts, user, created_repair)
    repair_problem_recommendation_create(problems, user, created_repair)

    return created_repair

def repair_spare_part_recommendation_create(spare_parts, user, created_repair):
    if spare_parts:
        for spare_part_id in spare_parts.split(','):
            spare_part_obj = get_object(SparePart, pk=spare_part_id)
            repair_sparepart_recommendation = RepairSparePartRecommendation(
                repair=created_repair,
                sparepart=spare_part_obj,
                added_by=user
            )
            repair_sparepart_recommendation.full_clean()
            repair_sparepart_recommendation.save()

def repair_problem_recommendation_create(problems, user, created_repair):
    if problems:
        for problem_id in problems.split(','):
            repair_problem = get_object(RepairProblem, pk=problem_id)
            repair_problem_recommendation = RepairProblemRecommendation(
                repair=created_repair,
                problem=repair_problem,
                added_by=user
            )
            repair_problem_recommendation.full_clean()
            repair_problem_recommendation.save()


