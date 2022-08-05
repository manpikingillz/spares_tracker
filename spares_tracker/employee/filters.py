import django_filters

from spares_tracker.employee.models import Employee

class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fileds = ('first_name', 'last_name', 'email','phone_number')