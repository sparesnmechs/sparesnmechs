from django.contrib import admin

from . import models


class MechanicAdmin(admin.ModelAdmin):
    """Admin appearance."""

    list_display = (
        "first_name",
        "last_name",
        "phone_number",
        "store",
    )

    # def get_specialities(self, obj):
    #     """Display specialities."""
    #     return ",".join([s.speciality for s in obj.specialities.all()])


class SpecialityAdmin(admin.ModelAdmin):
    """Admin appearance."""

    list_display = ("name", "car_make", "is_featured")


admin.site.register(models.Mechanic, MechanicAdmin)
admin.site.register(models.Speciality, SpecialityAdmin)
