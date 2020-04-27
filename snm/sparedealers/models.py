"""Models."""
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from snm.carowners.models import CarMake, CarModel


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

    class Meta:
        """Rep in its correct plural."""

        verbose_name_plural = "sparepart categories"

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class SparePartSubCategory(models.Model):
    """Spare part subcategory for each category created."""

    category = models.ForeignKey(SparePartCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        """Represent in its correct plural."""

        verbose_name_plural = "sparepart subcategories"

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

    dealer = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=14, decimal_places=2)
    condition = models.CharField(max_length=255, choices=CONDITION_CHOICES)
    year_of_manufacture = models.CharField(
        max_length=4,
        validators=[
            RegexValidator(regex="[0-9,]", message="Enter a valid year"),
        ],
    )
    category = models.ForeignKey(
        SparePartCategory,
        on_delete=models.PROTECT,
        related_name="part_categories",
    )
    sub_category = models.ForeignKey(
        SparePartSubCategory,
        on_delete=models.PROTECT,
        related_name="part_subcategories",
    )
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/")  # Only for development
    is_featured = models.BooleanField(default=False)

    # AD contact infomation
    phone_number = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex="^07[0-9]", message="Enter a valid phone number"
            ),
            MinLengthValidator(
                limit_value=10, message="Phone number should have 10 values"
            ),
        ],
    )
    first_name = models.CharField(max_length=20, blank=True, null=True)
    last_name = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=100)
    store = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name
