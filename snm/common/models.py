"""Models."""
from django.db import models


class Store(models.Model):
    """Create stores.

    Sparedealers have stores. These stores have a name and
    description defined in class CommonFields
    """

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        """Represent name for human readability."""
        return self.name
