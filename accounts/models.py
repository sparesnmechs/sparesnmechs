"""Create models for spare dealers, mechanics and car owners."""
from django.db import models
from common.models import Person


class SpareDealers(Person):
    """Create fields for spare dealers."""
    store_name = models.CharField(
        max_length=255, unique=True)  # What if the store has branches...should it have its own app
    # posts = models.ForeignKey() TODO Implement the posts app


class Mechanic(Person):
    """Create fields for mechanics."""
    garage_name = models.CharField(
        max_length=255, unique=True)  # Same comments as store
    # speciality = models.ForeignKey() TODO Implement in posts app


class CarOwner(Person):
    """Creates fields for a customer."""
    pass
    # TODO Discuss on car owners fields.
