"""Car owner model."""
from django.db import models


class CarMake(models.Model):
    """
    Create a make for a car.

    Car make has a name and description (optional). For example:
    name: Toyota.
    """

    photo = models.ImageField(upload_to="spareparts/car_make")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class CarModel(models.Model):
    """
    Create a car model.

    Every car make has a car model which has a name and an optional
    description eg. Toyota - Harrier.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/car_model")
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class CarOwner(models.Model):
    """Create a car onwer."""

    car_make = models.ManyToManyField(CarMake)
    car_model = models.ManyToManyField(CarModel)
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
