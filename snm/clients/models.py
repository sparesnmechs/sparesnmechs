"""Clients include sparedealers, mechanics and car owners."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from snm.spareparts.models import (CarMake, CarModel, CommonFields, SparePart,
                                   Speciality)


class Common(models.Model):
    """Common fields.
    
    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    description = models.TextField()
    photo = models.ImageField(upload_to="spareparts/")

    def __str__(self):
        """Represent first and last name for human readability."""
        return "{} {}".format(self.first_name, self.last_name)


class Store(CommonFields):
    """Create stores.

    Sparedealers have stores. These stores have a name and 
    description defined in class CommonFields
    """


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
