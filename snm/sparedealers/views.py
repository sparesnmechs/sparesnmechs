"""Views."""
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import SparePartFilter
from .models import SparePart, SparePartCategory


class SparePartCreateView(CreateView):
    """Create view for spare parts."""

    model = SparePart
    fields = [
        "name",
        "description",
        "price",
        "condition",
        "year_of_manufacture",
        "category",
        "sub_category",
        "car_make",
        "car_model",
    ]


class SparePartUpdateView(UpdateView):
    """Update view for spare parts."""

    model = SparePart
    fields = [
        "name",
        "description",
        "price",
        "condition",
        "year_of_manufacture",
        "category",
        "sub_category",
        "car_make",
        "car_model",
    ]


class SparePartDeleteView(DeleteView):
    """Delete a sparepart."""

    model = SparePart
    # success_url = reverse_lazy("#")  # TODO Create List View


class SparePartListView(ListView):
    """List view of spareparts."""

    queryset = SparePart.objects.all()
    context_object_name = "spareparts"


class SparePartCategoryListView(ListView):
    """List view of spareparts."""

    queryset = SparePartCategory.objects.all()
    context_object_name = "sparepart_category"
    template_name = "spareparts/sparepart_list.html"


def sparepart_view(request):
    """Search view."""
    spareparts_filter = SparePartFilter(
        request.GET, queryset=SparePart.objects.all()
    )
    return render(
        request, "sparedealers/sparepart_list.html", {"filter": spareparts_filter}
    )
