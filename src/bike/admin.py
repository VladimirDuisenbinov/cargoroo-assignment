from typing import Tuple

from django.contrib import admin

from .models import Bike


@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "fleet",
        "status",
        "location",
        "created",
        "updated",
        "archived",
    )
    inlines: Tuple = tuple(admin.ModelAdmin.inlines)
    readonly_fields: Tuple = admin.ModelAdmin.readonly_fields + (
        "id",
        "created",
        "updated",
        "archived",
    )
