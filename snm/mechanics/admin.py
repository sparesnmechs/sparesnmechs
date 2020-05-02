from django.contrib import admin

from . import models


class SpecialityAdmin(admin.ModelAdmin):
    """Admin appearance."""

    list_display = ["speciality"]


admin.site.register(models.Speciality, SpecialityAdmin)


class MechanicAdmin(admin.ModelAdmin):
    """Admin appearance."""

    list_display = (
        "first_name",
        "last_name",
        "specialities",
        "car_makes",
        "garage",
        "location",
    )


admin.site.register(models.Mechanic, MechanicAdmin)
