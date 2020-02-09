"""Car owner admin."""
from django.contrib import admin

from . import models

admin.site.register(models.CarOwner)
admin.site.register(models.CarMake)
admin.site.register(models.CarModel)
