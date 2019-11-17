"""Clients include sparedealers, mechanics and car owners."""
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from spareparts.models import (CarMake, CarModel, CommonFields, SparePart,
                               Speciality)


class Store(CommonFields):
    """Create a store for spare dealers."""


class SpareDealer(models.Model):
    """Create the spare dealer."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    description = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    spare_parts = models.ForeignKey(SparePart, on_delete=models.PROTECT)


class Mechanic(models.Model):
    """Create the mechanic."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    description = models.TextField()
    store = models.ForeignKey(Store, on_delete=models.PROTECT)
    speciality = models.ForeignKey(Speciality, on_delete=models.PROTECT)


class CarOwner(models.Model):
    """Create a car onwer."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = PhoneNumberField(blank=False)
    car_make = models.ForeignKey(CarMake, on_delete=models.PROTECT)
    car_model = models.ForeignKey(CarModel, on_delete=models.PROTECT)
