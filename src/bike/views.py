from typing import Tuple

from django_filters.rest_framework import DjangoFilterBackend

from core.custom_views import CustomViewSet

from .filters import BikeFilter
from .models import Bike
from .serializers import BikeSerializer


class BikeViewSet(CustomViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = BikeSerializer
    queryset = Bike.objects.filter(archived=False).order_by("-id")
    filter_backends: Tuple = (DjangoFilterBackend, )
    filterset_class = BikeFilter
