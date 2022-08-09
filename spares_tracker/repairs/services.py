from django.db import transaction
from spares_tracker.repairs.models import Repair
from spares_tracker.common.utils import get_object


#  Repair services.
@transaction.atomic
def repair_create(
    *,
    vehicle,
    problem_description,
    solution_description,
    spare_parts=None,
    problems=None,
) -> Repair:
    repair = Repair(
        vehicle=vehicle,
        problem_description=problem_description,
        solution_description=solution_description,
    )

    repair.full_clean()
    repair.save()

    created_repair = get_object(Repair, pk=repair.id)

    if spare_parts:
        _spare_parts = spare_parts.split(',')
        created_repair.spare_parts.add(*_spare_parts)

    if problems:
        _problems = problems.split(',')
        created_repair.problems.add(*_problems)

    return created_repair


