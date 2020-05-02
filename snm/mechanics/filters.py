"""Filter spareparts."""
import django_filters

from .models import Mechanic
from django.forms.widgets import TextInput


class MechanicFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    location = django_filters.CharFilter(
        widget=TextInput(attrs={"placeholder": "Location"})
    )

    class Meta:
        """Meta."""

        model = Mechanic
        fields = {
            "car_make": ["exact"],
            "speciality": ["exact"],
            "location": ["exact"],
        }

    def __init__(self, *args, **kwargs):
        super(MechanicFilter, self).__init__(*args, **kwargs)
        self.filters["car_make"].label = ""
        self.filters["speciality"].label = ""
        self.filters["location"].label = ""
