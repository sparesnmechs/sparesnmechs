"""Speciality app admin."""
from django.contrib import admin

import snm.specialities.models as models

admin.site.register(models.Speciality)
admin.site.register(models.CarMake)
admin.site.register(models.CarModel)
