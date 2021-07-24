"""Common managers."""
from datetime import datetime

from django.db import models
from django.db.models.query import QuerySet


class SoftDeletionQuerySet(QuerySet):
    """Django soft deletion query set."""

    def delete(self):
        """Bulk soft deleting a QuerySet."""
        return super(SoftDeletionQuerySet, self).update(
            deleted_at=datetime.now()
        )

    def hard_delete(self):
        """Bulk hard deleting a QuerySet."""
        return super(SoftDeletionQuerySet, self).delete()


class SoftDeletionManager(models.Manager):
    """Soft deletion Django custom manager."""

    def __init__(self, *args, **kwargs):
        """Initialize with alive_only set to True by default."""
        self.alive_only = kwargs.pop("alive_only", True)
        super(SoftDeletionManager, self).__init__(*args, **kwargs)

    def get_queryset(self):
        """Queryset to return all/only deleted objects."""
        if self.alive_only:
            return SoftDeletionQuerySet(self.model).filter(deleted_at=None)
        return SoftDeletionQuerySet(self.model)

    def hard_delete(self):
        """Allow us to truly delete a queryset."""
        return self.get_queryset().hard_delete()
