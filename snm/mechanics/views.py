"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import SpecialityFilter
from .models import Mechanic, Speciality


class SpecialityListView(ListView):
    """List view of spareparts."""

    queryset = Speciality.objects.all()
    context_object_name = "speciality"


class SpecialityCreateView(LoginRequiredMixin, CreateView):
    """Create view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"


class SpecialityUpdateView(LoginRequiredMixin, UpdateView):
    """Update view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"


class SpecialityDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = Speciality
    login_url = "login"
    redirect_field_name = "redirect_to"


class MechanicCreateView(LoginRequiredMixin, CreateView):
    """Create view for mechanics."""

    model = Mechanic
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "store",
        "description",
        "photo",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"


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
