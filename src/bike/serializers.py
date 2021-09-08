from rest_framework import serializers

from core.custom_api_exception import CustomApiException

from .choices import BIKE_STATUS_CHOICES
from .models import Bike


class LocationSerializer(serializers.Serializer):
    latitude = serializers.DecimalField(
        required=True, max_digits=20, decimal_places=17
    )
    longitude = serializers.DecimalField(
        required=True, max_digits=21, decimal_places=17
    )

    def validate(self, data):
        if 'latitude' in data:
            data['latitude'] = str(data['latitude'])
        if 'longitude' in data:
            data['longitude'] = str(data['longitude'])

        return data

    def validate_latitude(self, value):
        if int(value) < -90 or int(value) > 90:
            message = 'Latitude should be less than 90 and more than -90.'
            raise CustomApiException(status_code=400, message=message)

        return super().validate(value)

    def validate_longitude(self, value):
        if int(value) < -180 or int(value) > 80:
            message = 'Longitude should be less than 80 and more than -180.'
            raise CustomApiException(status_code=400, message=message)

        return super().validate(value)


class BikeSerializer(serializers.ModelSerializer):
    status = serializers.ChoiceField(required=True, choices=BIKE_STATUS_CHOICES)
    location = LocationSerializer(required=True)

    class Meta:
        model = Bike
        exclude = ("created", "updated", "archived")
