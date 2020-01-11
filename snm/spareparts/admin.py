from django.contrib import admin

from . import models

admin.site.register(models.SparePart)
admin.site.register(models.SparePartCategory)
admin.site.register(models.SparePartSubCategory)
admin.site.register(models.Speciality)
admin.site.register(models.CarMake)
admin.site.register(models.CarModel)
admin.site.register(models.SpareDealer)
admin.site.register(models.Mechanic)
admin.site.register(models.Store)
admin.site.register(models.FeaturedSparePart)
admin.site.register(models.FeaturedSpeciality)
