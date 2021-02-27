"""Spareparts app models."""
from django.db import models

from snm.userprofiles.models import UserProfile


class SparePartCategory(models.Model):
    """Holds the basic information of a sparepart category."""

    name = models.CharField(max_length=20)

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name


class SparePartSubCategory(models.Model):
    """Holds the basic information of a sparepart sub-category."""

    name = models.CharField(max_length=20)
    category = models.ForeignKey(SparePartCategory, on_delete=models.CASCADE)

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name


class SparePart(models.Model):
    """Holds the basic information of a sparepart."""

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    condition = models.CharField(
        choices=[
            ("new", "New"),
            ("locally_used", "Locally Used"),
            ("foreign_used", "Foreign Used"),
        ],
        max_length=20,
        default="locally_used",
    )
    price = models.DecimalField(max_digits=20, decimal_places=4)
    category = models.ForeignKey(SparePartCategory, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(
        SparePartSubCategory, on_delete=models.CASCADE
    )

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name
