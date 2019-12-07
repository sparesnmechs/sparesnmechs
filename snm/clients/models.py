"""Clients include sparedealers, mechanics and car owners."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from snm.spareparts.models import (CarMake, CarModel, CommonFields, SparePart,
                                   Speciality)


class Common(models.Model):
    """Common fields."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    description = models.TextField()
    photo = models.ImageField(upload_to="spareparts/")

    def __str__(self):
        """Represent first and last name."""
        return "{} {}".format(self.first_name, self.last_name)


class Store(CommonFields):
    """Create a store for spare dealers."""


class SpareDealer(Common):
    """Create the spare dealer."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    spare_parts = models.ForeignKey(SparePart, on_delete=models.PROTECT)


class Mechanic(Common):
    """Create the mechanic."""

    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT)


class CarOwner(Common):
    """Create a car onwer."""

    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
