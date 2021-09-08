from django_filters import CharFilter, FilterSet

from .models import Fleet


class FleetFilter(FilterSet):
    name = CharFilter(field_name="name", lookup_expr="icontains")

    class Meta:
        model = Fleet
        fields = ('name', )
