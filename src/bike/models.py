from django.db import models
from django.db.models import Manager

from fleet.models import Fleet

from .choices import BIKE_STATUS_CHOICES


def generate_id() -> str:
    delimiter = 'BK_'
    last_id = 0

    bikes = Bike.objects.order_by('-id')
    if len(bikes) > 0:
        last_bike = bikes.first()
        last_id = int(last_bike.id.split(delimiter)[1])

    next_id = last_id + 1
    if next_id < 10:
        next_id = '00' + str(next_id)
    elif next_id < 100:
        next_id = '0' + str(next_id)

    return delimiter + next_id


class Bike(models.Model):
    id = models.CharField(
        verbose_name="id", help_text="id", primary_key=True,
        default=generate_id, editable=False, max_length=6
    )
    fleet = models.ForeignKey(
        to=Fleet, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="fleet", help_text="fleet", related_name="bike"
    )
    status = models.CharField(
        verbose_name="status", help_text="status", choices=BIKE_STATUS_CHOICES,
        null=False, blank=False, max_length=8
    )
    # Validation is on a serializer level
    location = models.JSONField(
        verbose_name="location", help_text="location"
    )
    created = models.DateTimeField(
        auto_now_add=True, help_text="created", verbose_name="created"
    )
    updated = models.DateTimeField(
        auto_now=True, help_text="updated", verbose_name="updated"
    )
    archived = models.BooleanField(
        default=False, help_text="archived", verbose_name="archived"
    )
    objects: Manager

    class Meta:
        app_label = "bike"
        db_table = "bike.bikes"
        verbose_name = "bike"
        verbose_name_plural = "bikes"
