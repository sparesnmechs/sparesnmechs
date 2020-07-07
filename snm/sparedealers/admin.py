from django.contrib import admin

from . import models


class SparePartSubCategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "category")


admin.site.register(models.SparePart)
admin.site.register(models.SparePartCategory)
admin.site.register(models.Condition)
admin.site.register(models.SparePartSubCategory, SparePartSubCategoryAdmin)
