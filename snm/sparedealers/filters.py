"""Filter spareparts."""
import django_filters

from .models import SparePart


class SparePartFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    class Meta:
        """Meta."""

        model = SparePart
        fields = {
            "category": ["exact"],
            "sub_category": ["exact"],
            "car_make": ["exact"],
            "car_model": ["exact"],
            "condition": ["exact"],
            "year_of_manufacture": ["lt", "gt",],
        }
