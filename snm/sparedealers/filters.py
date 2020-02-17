"""Filter spareparts."""
import django_filters

from .models import SparePart


class SparePartFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    class Meta:
        """Meta."""

        model = SparePart
        fields = [
            "car_make",
            "car_model",
            "category",
            "sub_category",
            "year_of_manufacture",
            "condition",
        ]
