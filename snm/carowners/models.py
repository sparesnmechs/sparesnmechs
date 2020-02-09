"""Car owner model."""
from django.db import models

from snm.common.models import CommonItemFields, CommonUserFields


class CarMake(CommonItemFields):
    """
    Create a make for a car.

    Car make has a name and description (optional). For example:
    name: Toyota.
    """

    photo = models.ImageField(upload_to="spareparts/car_make")


class CarModel(CommonItemFields):
    """
    Create a car model.

    Every car make has a car model which has a name and an optional
    description eg. Toyota - Harrier.
    """

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to="spareparts/car_model")


class CarOwner(CommonUserFields):
    """Create a car onwer."""

    car_make = models.ManyToManyField(CarMake)
    car_model = models.ManyToManyField(CarModel)
