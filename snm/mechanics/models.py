"""Models."""
from django.db import models

from snm.carowners.models import CarMake


class Speciality(models.Model):
    """
    Create fields for mechanic specialities.

    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)  # Half Baked

    class Meta:
        """Speciality in its correct plural."""

        verbose_name_plural = "specialities"

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class Mechanic(models.Model):
    """Create the mechanic."""

    store = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=10
    )  # Validate to accept phone no
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="spareparts/", blank=True, null=True)
    specialities = models.ManyToManyField(Speciality)

    def __str__(self):
        """Represent first and last name for human readability."""
        return "{} {}".format(self.first_name, self.last_name)
