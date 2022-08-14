from spares_tracker.common.utils import get_object
from spares_tracker.employee.models import Employee, Section, Station
from django.db.models.query import QuerySet
from spares_tracker.employee.filters import BaseEmployeeFilter,  BaseStationFilter


def employee_list(*, filters=None) -> QuerySet[Employee]:
    filters = filters or {}

    qs = Employee.objects.filter(removed=False)
    return BaseEmployeeFilter(filters, qs).qs


def employee_detail(*, pk) -> Employee:
    return get_object(Employee, pk=pk)


def station_list(*, filters=None) -> QuerySet[Station]:
    filters = filters or {}

    qs = Station.objects.filter(removed=False)
    return BaseStationFilter(filters, qs).qs

def section_list(*, filters=None) -> QuerySet[Section]:
    filters = filters or {}

    qs = Section.objects.filter(removed=False)
    return BaseStationFilter(filters, qs).qs