"""Spare parts and speciality model."""
from django.db import models


class CommonFields(models.Model):
    """Common fields.
    
    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        """Represent name for human readability."""
        return self.name

    class Meta:
        """Make this class an abstract class."""

        abstract = True


class SparePartCategory(CommonFields):
    """
    Create the categories for spare parts.
    
    The sparepart category has a name and description field
    obtianed from class CommonField
    """


class SparePartSubCategory(CommonFields):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(SparePartCategory, on_delete=models.PROTECT)

    def __str__(self):
        """Represent a spare part subcategory name."""
        return self.name


class CarMake(CommonFields):
    """
    Create a make for a car.
    
    Car make has a name and description (optional). For example:
    name: Toyota.
    """


class CarModel(CommonFields):
    """
    Create a car model.
    
    Every car make has a car model which has a name and an optional
    description eg. Toyota - Harrier.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)


class Speciality(CommonFields):
    """
    Create fields for mechanic specialities.
    
    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)


class SparePart(CommonFields):
    """
    Create fields for spare parts.
    
    Sparedealers deal with selling spareparts to car owners. Eg. Bumper
    """

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
