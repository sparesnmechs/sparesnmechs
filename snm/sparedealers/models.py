from django.db import models

from snm.common.models import CommonItemFields, CommonUserFields, Store
from snm.carowners.models import CarMake, CarModel


class SpareDealer(CommonUserFields):
    """Create the spare dealer."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)


class SparePartCategory(CommonItemFields):
    """
    Create the categories for spare parts.

    The sparepart category has a name and description field
    obtianed from class CommonField
    """

    photo = models.ImageField(upload_to="spareparts/category")


class SparePartSubCategory(CommonItemFields):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)

    def __str__(self):
        """Represent a spare part subcategory name."""
        return self.name


class SparePart(CommonItemFields):
    """
    Create fields for spare parts.

    Sparedealers deal with selling spareparts to car owners. Eg. Bumper
    """

    CONDITION_CHOICES = [
        ("NEW", "New"),
        ("LOCALLY USED", "Locally Used"),
        ("FOREIGN USED", "Foreign Used"),
    ]

    sparedealer = models.ForeignKey(SpareDealer, on_delete=models.PROTECT)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    year_of_manufacture = models.CharField(max_length=225)
    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(
        SparePartSubCategory, on_delete=models.PROTECT
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/")  # Only for development
    is_featured = models.BooleanField(default=False)
