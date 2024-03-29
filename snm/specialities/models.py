"""Speciality app models."""
from django.db import models

from snm.common.models import AbstractBase, AbstractListingBase
from snm.userprofiles.models import UserProfile


class CarMake(AbstractBase):
    """Holds the basic information of a car make eg. Toyota."""

    name = models.CharField(max_length=20)

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name


class CarModel(AbstractBase):
    """Holds the basic information of a car model eg Toyota Harrier."""

    name = models.CharField(max_length=20)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name


class Speciality(AbstractListingBase):
    """Holds the basic information of a Speciality."""

    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete=models.CASCADE)

    def __str__(self):
        """Represent the class object in a human readable form."""
        return self.name
