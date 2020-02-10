"""Filter speciality."""
import django_filters

from .models import Speciality


class SpecialityFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    class Meta:
        """Meta."""

        model = Speciality
        fields = [
            "mechanic",
            "car_make",
        ]
