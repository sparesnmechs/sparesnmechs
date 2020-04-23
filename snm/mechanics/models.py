"""Models."""
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from snm.carowners.models import CarMake


class Speciality(models.Model):
    """
    Create fields for mechanic specialities.

    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    mechanic = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    is_featured = models.BooleanField(default=False)  # Half Baked
    price = models.DecimalField(max_digits=14, decimal_places=2)

    # Contact information
    store = models.CharField(max_length=100, blank=True, null=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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
    photo = models.ImageField(upload_to="mechanic/", blank=True, null=True)
    region = models.CharField(max_length=20)
    place = models.CharField(max_length=20)

    class Meta:
        """Speciality in its correct plural."""

        verbose_name_plural = "specialities"

    def __str__(self):
        """Represent name for human readability."""
        return self.name
