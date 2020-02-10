"""Models."""
from django.db import models


class CommonUserFields(models.Model):
    """Common fields.

    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

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


class CommonItemFields(models.Model):
    """Common fields.

    These fields are common to most models hence they are
    defined here to follow the DRY rule
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name


class Store(CommonItemFields):
    """Create stores.

    Sparedealers have stores. These stores have a name and
    description defined in class CommonFields
    """
