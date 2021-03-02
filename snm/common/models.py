"""Common models."""
import uuid

from django.db import models
from django.utils import timezone


class AbstractBase(models.Model):
    """Fields common to all models."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(default=timezone.now)

    class Meta:
        """Define meta options."""

        abstract = True
