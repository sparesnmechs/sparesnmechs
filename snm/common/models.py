"""Common models."""
import uuid
from datetime import datetime

from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from snm.common.managers import SoftDeletionManager


class AbstractBase(models.Model):
    """Fields common to all models."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())
    created_by = models.UUIDField(blank=True, null=True)
    updated_by = models.UUIDField(blank=True, null=True)

    class Meta:
        """Define meta options."""

        abstract = True


class AbstractCustomUser(AbstractBaseUser, AbstractBase):
    """Abstract base custom user."""

    class Meta:
        """Define meta options."""

        abstract = True


class AbstractSoftDeletion(models.Model):
    """Abstract soft deletion model."""

    deleted_at = models.DateTimeField(blank=True, null=True)
    objects = SoftDeletionManager()
    all_objects = SoftDeletionManager(alive_only=False)

    class Meta:
        """Define meta options."""

        abstract = True

    def delete(self):
        """Soft delete a django object."""
        self.deleted_at = datetime.now()
        self.save()

    def hard_delete(self):
        """Permanently remove an object from the database."""
        super(AbstractSoftDeletion, self).delete()


class AbstractListingBase(AbstractBase, AbstractSoftDeletion):
    """Field common to all sparesnmechs listings."""

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        """Define meta options."""

        abstract = True
