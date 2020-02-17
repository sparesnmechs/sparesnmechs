"""Models."""
from django.db import models

from snm.common.models import Store
from snm.carowners.models import CarMake, CarModel


class SpareDealer(models.Model):
    """Create the spare dealer."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10
    )  # Validate to accept phone no
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="spareparts/")

    def __str__(self):
        """Represent first and last name for human readability."""
        return "{} {}".format(self.first_name, self.last_name)


class SparePartCategory(models.Model):
    """
    Create the categories for spare parts.

    The sparepart category has a name and description field
    obtianed from class CommonField
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="spareparts/category", blank=True, null=True
    )

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class SparePartSubCategory(models.Model):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(
        SparePartCategory,
        on_delete=models.PROTECT,
        related_name="sparepartcategories",
    )
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class SparePart(models.Model):
    """
    Create fields for spare parts.

    Sparedealers deal with selling spareparts to car owners. Eg. Bumper
    """

    CONDITION_CHOICES = [
        ("NEW", "New"),
        ("LOCALLY USED", "Locally Used"),
        ("FOREIGN USED", "Foreign Used"),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
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

    def __str__(self):
        """Represent name for human readability."""
        return self.name
