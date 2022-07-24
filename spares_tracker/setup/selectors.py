from django.db.models.query import QuerySet
from spares_tracker.setup.models import Country


def country_list() -> QuerySet[Country]:
    return Country.objects.all()