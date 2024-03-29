import django_filters

from spares_tracker.employee.models import Employee, Station

class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email','phone_number')

class BaseStationFilter(django_filters.FilterSet):
    class Meta:
        model = Station
        fields = ('name', )