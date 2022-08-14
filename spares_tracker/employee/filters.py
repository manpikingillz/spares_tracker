import django_filters

from spares_tracker.employee.models import Employee, Section, Station

class BaseEmployeeFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'email','phone_number', 'station', 'section')

class BaseStationFilter(django_filters.FilterSet):
    class Meta:
        model = Station
        fields = ('name', )

class BaseSectionFilter(django_filters.FilterSet):
    class Meta:
        model = Section
        fields = ('name', )