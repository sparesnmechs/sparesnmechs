"""Common fields for models."""
from django.db import models
from phone_field import PhoneField


class Person(models.Model):
    """Common fields for all accounts."""

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True)
    photo = models.ImageField(upload_to='images/')
    phone_number = PhoneField(help_text='Phone Number')
    # TODO Integrate location with Google Maps
    # TODO Split profile photos and Product photos

    def __str__(self):
        """Person string representation."""
        return '{} {}'.format(self.first_name, self.last_name)

    class Meta:
        """Abstract."""

        abstract = True


class CommonFields(models.Model):
    """Common fields for most models."""

    name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        """Abstract."""

        abstract = True
