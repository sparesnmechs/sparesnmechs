from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

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
