from django.db import transaction
from spares_tracker.repairs.models import Repair


#  Repair services.
@transaction.atomic
def repair_create(
    *,
    vehicle,
    problem_description,
    solution_description,
    spare_parts,
    problems,
) -> Repair:
    repair = Repair(
        vehicle=vehicle,
        problem_description=problem_description,
        solution_description=solution_description,
    )

    repair.full_clean()
    repair.save()

    _spare_parts = spare_parts.split(',')
    _problems = problems.split(',')

    repair.spare_parts.add(*_spare_parts)
    repair.problems.add(*_problems)

    return repair


