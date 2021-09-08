from rest_framework import serializers

from .models import Fleet


class FleetSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True, max_length=255)

    class Meta:
        model = Fleet
        exclude = ("created", "updated", "archived")
