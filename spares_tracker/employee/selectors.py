from spares_tracker.common.utils import get_object
from spares_tracker.employee.models import Employee
from django.db.models.query import QuerySet
from spares_tracker.employee.filters import BaseEmployeeFilter


def employee_list(*, filters=None) -> QuerySet[Employee]:
    filters = filters or {}

    qs = Employee.objects.filter(removed=False)
    return BaseEmployeeFilter(filters, qs).qs


def employee_detail(*, pk) -> Employee:
    return get_object(Employee, pk=pk)