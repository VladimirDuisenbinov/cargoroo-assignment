from django.db import models
from django.db.models import Manager


def generate_id() -> str:
    delimiter = 'FL_'
    last_id = 0

    fleets = Fleet.objects.order_by('-id')
    if len(fleets) > 0:
        last_fleet = fleets.first()
        last_id = int(last_fleet.id.split(delimiter)[1])

    next_id = last_id + 1
    if next_id < 10:
        next_id = '00' + str(next_id)
    elif next_id < 100:
        next_id = '0' + str(next_id)

    return delimiter + next_id


class Fleet(models.Model):
    id = models.CharField(
        verbose_name="id", help_text="id", primary_key=True,
        default=generate_id, editable=False, max_length=6
    )
    name = models.CharField(
        verbose_name="name", help_text="name", max_length=255
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
        app_label = "fleet"
        db_table = "fleet.fleets"
        verbose_name = "fleet"
        verbose_name_plural = "fleets"
