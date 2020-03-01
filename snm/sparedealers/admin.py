from django.contrib import admin

from . import models

admin.site.register(models.SparePart)
admin.site.register(models.SparePartCategory)
admin.site.register(models.SparePartSubCategory)
