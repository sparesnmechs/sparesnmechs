"""Spare parts and speciality model."""
from django.db import models

from common.models import CommonFields


class SparePart(CommonFields):
    """Create fields for spare parts."""

    CONDITION_CHOICES = [
        ('NEW', 'New'),
        ('LOCALLY USED', 'Locally Used'),
        ('FOREIGN USED', 'Foreign Used'),
    ]

    price = models.DecimalField(max_digits=14, decimal_places=2)
    condition = models.CharField(
        max_length=255, choices=CONDITION_CHOICES)
    year_of_manufacture = models.DateField(
        verbose_name="Year(s) of manufacture (YYYY-MM-DD)")
    category = models.ForeignKey(
        'SparePartCategory', on_delete=models.PROTECT)
    sub_category = models.ForeignKey(
        'SparePartSubCategory', on_delete=models.PROTECT)
    car_make = models.ForeignKey('CarMake', on_delete=models.PROTECT)
    car_model = models.ForeignKey('CarModel', on_delete=models.PROTECT)
    # TODO Implement a gallery - More work on the templates

    def __str__(self):
        """Represent a spare part name."""
        return self.name


class SparePartCategory(CommonFields):
    """Create the categories for spare parts."""

    def __str__(self):
        """Represent a spare part category name."""
        return self.name


class SparePartSubCategory(CommonFields):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey('SparePartCategory', on_delete=models.PROTECT)

    def __str__(self):
        """Represent a spare part subcategory name."""
        return self.name


class Speciality(CommonFields):
    """Create fields for mechanic specialities."""

    car_make = models.ForeignKey('CarMake', on_delete=models.PROTECT)

    def __str__(self):
        """Represent a speciality using its name."""
        return self.name


class CarMake(CommonFields):
    """Every car has a make eg. Toyota."""

    def __str__(self):
        """Represent a car make name."""
        return self.name


class CarModel(CommonFields):
    """Every car make has a car model eg. Toyota - Harrier."""

    car_make = models.ForeignKey('CarMake', on_delete=models.PROTECT)

    def __str__(self):
        """Represent a car model name."""
        return self.name
