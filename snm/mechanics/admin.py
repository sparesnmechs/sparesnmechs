from django.contrib import admin

from . import models


class SpecialityAdmin(admin.ModelAdmin):
    """Admin appearance."""

    list_display = ("name", "car_make", "is_featured")


admin.site.register(models.Speciality, SpecialityAdmin)
