"""Common fields for models."""
from django.db import models


class Person(models.Model):
    """An Abstract Base class model that provides first_name and last_name fields for all the users."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='images/')
    # TODO Integrate location with Google Maps

    def __str__(self):
        """Person string representation."""
        return '{} {}'.format(first_name, last_name)

    class Meta:
        abstract = True
