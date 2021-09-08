from typing import Tuple

from django_filters.rest_framework import DjangoFilterBackend

from core.custom_views import CustomViewSet

from .filters import FleetFilter
from .models import Fleet
from .serializers import FleetSerializer


class FleetViewSet(CustomViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = FleetSerializer
    queryset = Fleet.objects.filter(archived=False).order_by("-id")
    filter_backends: Tuple = (DjangoFilterBackend, )
    filterset_class = FleetFilter
