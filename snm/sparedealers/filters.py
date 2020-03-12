"""Filter spareparts."""
import django_filters

from .models import SparePart


class SparePartFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    class Meta:
        """Meta."""

        model = SparePart
        fields = [
            "category",
            "sub_category",
            "car_make",
            "car_model",
            "condition",
        ]
