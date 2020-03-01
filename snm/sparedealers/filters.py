"""Filter spareparts."""
import django_filters

from .models import SparePartCategory


class SparePartCategoryFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    class Meta:
        """Meta."""

        model = SparePartCategory
        fields = [
            "sub_category",
        ]
