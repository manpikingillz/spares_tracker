import django_filters

from spares_tracker.users.models import BaseUser


class BaseUserFilter(django_filters.FilterSet):
    class Meta:
        model = BaseUser
        fields = ('id', 'email', 'is_admin')
