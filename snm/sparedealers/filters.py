"""Filter spareparts."""
import django_filters

from .models import SparePart
from django.forms.widgets import TextInput


class SparePartFilter(django_filters.FilterSet):
    """Filterset for spareparts."""

    year_of_manufacture__lt = django_filters.CharFilter(
        widget=TextInput(attrs={"placeholder": "Year: Min"})
    )
    year_of_manufacture__gt = django_filters.CharFilter(
        widget=TextInput(attrs={"placeholder": "Year: Max"})
    )

    class Meta:
        """Meta."""

        model = SparePart
        fields = {
            "category": ["exact"],
            "sub_category": ["exact"],
            "car_make": ["exact"],
            "car_model": ["exact"],
            "condition": ["exact"],
            "year_of_manufacture": ["lt", "gt"],
        }
        widgets = {
            "year_of_manufacture__lt": TextInput(
                attrs={"placeholder": "Year of Manufacture"}
            ),
            "year_of_manufacture__gt": TextInput(
                attrs={"placeholder": "Year of Manufacture"}
            ),
        }

    def __init__(self, *args, **kwargs):
        super(SparePartFilter, self).__init__(*args, **kwargs)
        self.filters["category"].extra.update({"empty_label": "Category"})
        self.filters["sub_category"].extra.update(
            {"empty_label": "Sub Category"}
        )
        self.filters["car_model"].extra.update({"empty_label": "Car Model"})
        self.filters["car_make"].extra.update({"empty_label": "Car Make"})
        self.filters["condition"].extra.update({"empty_label": "Condition"})

        self.filters["category"].label = ""
        self.filters["sub_category"].label = ""
        self.filters["car_model"].label = ""
        self.filters["car_make"].label = ""
        self.filters["condition"].label = ""
        self.filters["year_of_manufacture__lt"].label = ""
        self.filters["year_of_manufacture__gt"].label = ""
