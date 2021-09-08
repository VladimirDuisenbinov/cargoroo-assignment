from django_filters import CharFilter, ChoiceFilter, FilterSet

from .choices import BIKE_STATUS_CHOICES
from .models import Bike


class BikeFilter(FilterSet):
    fleet = CharFilter(field_name="fleet", lookup_expr="exact")
    status = ChoiceFilter(choices=BIKE_STATUS_CHOICES)
    latitude = CharFilter(field_name="location__latitude", lookup_expr="exact")
    longitude = CharFilter(
        field_name="location__longitude", lookup_expr="exact"
    )

    class Meta:
        model = Bike
        fields = ('fleet', 'status', 'latitude', 'longitude')
