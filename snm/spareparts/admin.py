"""Spareparts app Admin."""
from django.contrib import admin

import snm.spareparts.models as models

admin.site.register(models.SparePart)
admin.site.register(models.SparePartCategory)
admin.site.register(models.SparePartSubCategory)
