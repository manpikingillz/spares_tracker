from django.db import transaction
from django.core.exceptions import ValidationError
from spares_tracker.repairs.models import Repair, RepairProblem, RepairProblemRecommendation, RepairSparePartRecommendation
from spares_tracker.common.utils import get_object
from spares_tracker.spareparts.models import SparePart
from spares_tracker.common.services import model_update

REPAIR_INSTANCE_IS_NONE = f'You attempted updating a {Repair.__name__} that does not exist!'

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

    repair_sparepart_recommendation_create(spare_parts, user, created_repair)
    repair_problem_recommendation_create(problems, user, created_repair)

    return created_repair

def repair_sparepart_recommendation_create(spare_parts, user, created_repair):
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

def repair_sparepart_recommendation_update(repair, spareparts, added_by):
    if spareparts:
        RepairSparePartRecommendation.objects.filter(repair=repair).delete()
        for spare_part_id in spareparts.split(','):
            spare_part_obj = get_object(SparePart, pk=spare_part_id)

            repair_sparepart_recommendation = RepairSparePartRecommendation(
                repair=repair,
                sparepart=spare_part_obj,
                added_by=added_by
            )
            repair_sparepart_recommendation.full_clean()
            repair_sparepart_recommendation.save()

def repair_problem_recommendation_update(repair, problems, added_by):
    if problems:
        RepairProblemRecommendation.objects.filter(repair=repair).delete()
        for problem_id in problems.split(','):
            repair_problem = get_object(RepairProblem, pk=problem_id)

            repair_problem_recommendation = RepairProblemRecommendation(
                repair=repair,
                problem=repair_problem,
                added_by=added_by
            )
            repair_problem_recommendation.full_clean()
            repair_problem_recommendation.save()

@transaction.atomic
def repair_update(*, repair: Repair, data):
    model_fields = list(vars(repair).keys())
    model_fields.remove('id')

    for field in model_fields:
        if field == '_state':
            model_fields.remove('_state')

        if field.endswith('_id'):
            modified_field = field[:-3]
            model_fields.remove(field)
            model_fields.append(modified_field)

    if not repair:
        raise ValidationError(
            REPAIR_INSTANCE_IS_NONE
        )
    _repair, has_updated = model_update(
        instance=repair,
        fields=model_fields,
        data=data
    )

    return _repair


