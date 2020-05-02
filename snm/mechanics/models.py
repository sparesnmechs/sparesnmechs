"""Models."""
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models

from snm.carowners.models import CarMake


class Speciality(models.Model):
    """Make a list of specialitites."""

    speciality = models.CharField(max_length=100)

    class Meta:
        """Speciality in its correct plural."""

        verbose_name_plural = "specialities"

    def __str__(self):
        """Represent name for human readability."""
        return self.speciality


class Mechanic(models.Model):
    """
    Create fields for mechanic specialities.

    A mechanic has a special area where they are skilled in.
    For example Wiring.
    """

    mechanic = models.ForeignKey(User, on_delete=models.CASCADE)
    speciality = models.ManyToManyField(
        Speciality, related_name="specialities"
    )
    car_make = models.ManyToManyField(CarMake)
    is_featured = models.BooleanField(default=False)  # Half Baked

    # Contact information
    garage = models.CharField(max_length=100, blank=True, null=True)
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
    logo = models.ImageField(upload_to="mechanic/")
    location = models.CharField(max_length=100)

    def __str__(self):
        """Represent name for human readability."""
        return self.phone_number

    def specialities(self):
        return ", ".join(
            [str(speciality) for speciality in self.speciality.all()]
        )

    def car_makes(self):
        return ", ".join([str(car_make) for car_make in self.car_make.all()])
