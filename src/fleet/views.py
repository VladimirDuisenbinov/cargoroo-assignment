from typing import Tuple

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .filters import FleetFilter
from .models import Fleet
from .serializers import FleetSerializer


class FleetViewSet(ModelViewSet):
    http_method_names: Tuple = ("get", "post", "patch", "delete")
    serializer_class = FleetSerializer
    queryset = Fleet.objects.filter(archived=False).order_by("-id")
    filter_backends: Tuple = (DjangoFilterBackend, )
    filterset_class = FleetFilter

    def create(self, request: Request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer=serializer)
        return Response(data={"status": "success", "data": serializer.data})

    def retrieve(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(data={"status": "success", "data": serializer.data})

    def update(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        serializer = self.get_serializer(
            instance, data=request.data, partial=True
        )
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(data={"status": "success", "data": serializer.data})

    def destroy(self, request, *args, **kwargs) -> Response:
        instance = self.get_object()
        instance.archived = True
        instance.save(update_fields=["archived"])
        return Response(data={"status": "success"})
