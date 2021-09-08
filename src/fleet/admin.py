from typing import Tuple

from django.contrib import admin

from .models import Fleet


@admin.register(Fleet)
class FleetAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
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
