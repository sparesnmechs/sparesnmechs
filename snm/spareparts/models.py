"""Spare parts and speciality model."""
from django.db import models


class CommonFields(models.Model):
    """Common fields for most models."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Represent a name."""
        return self.name

    class Meta:
        """Abstract."""

        abstract = True


class SparePartCategory(CommonFields):
    """Create the categories for spare parts."""


class SparePartSubCategory(CommonFields):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)

    def __str__(self):
        """Represent a spare part subcategory name."""
        return self.name


class CarMake(CommonFields):
    """Every car has a make eg. Toyota."""


class CarModel(CommonFields):
    """Every car make has a car model eg. Toyota - Harrier."""

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)


class Speciality(CommonFields):
    """Create fields for mechanic specialities."""

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)


class SparePart(CommonFields):
    """Create fields for spare parts."""

    CONDITION_CHOICES = [
        ("NEW", "New"),
        ("LOCALLY USED", "Locally Used"),
        ("FOREIGN USED", "Foreign Used"),
    ]

    price = models.DecimalField(max_digits=14, decimal_places=2)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    year_of_manufacture = models.CharField(max_length=4)  # Validate
    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)
    sub_category = models.ForeignKey(SparePartSubCategory,
                                     on_delete=models.PROTECT)
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/")
