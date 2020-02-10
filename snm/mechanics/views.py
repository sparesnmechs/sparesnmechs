"""Views."""
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import SpecialityFilter
from .models import Speciality


class SpecialityListView(ListView):
    """List view of spareparts."""

    queryset = Speciality.objects.all()
    context_object_name = "speciality"


class SpecialityCreateView(CreateView):
    """Create view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]


class SpecialityUpdateView(UpdateView):
    """Update view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]


class SpecialityDeleteView(DeleteView):
    """Delete a sparepart."""

    model = Speciality
    # success_url = reverse_lazy("#")  # TODO Create List View


def speciality_view(request):
    """Search view."""
    speciality_filter = SpecialityFilter(
        request.GET, queryset=Speciality.objects.all()
    )
    return render(
        request,
        "mechanics/speciality_list.html",
        {"filter": speciality_filter},
    )
