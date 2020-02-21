"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .filters import SpecialityFilter
from .models import Mechanic, Speciality


class SpecialityListView(ListView):
    """List view of spareparts."""

    queryset = Speciality.objects.all()
    context_object_name = "speciality"


class SpecialityCreateView(
    SuccessMessageMixin, LoginRequiredMixin, CreateView
):
    """Create view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your speciality has been succesfully created"


class SpecialityUpdateView(
    SuccessMessageMixin, LoginRequiredMixin, UpdateView
):
    """Update view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your speciality has been succesfully updated"


class SpecialityDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = Speciality
    login_url = "login"
    redirect_field_name = "redirect_to"


class MechanicCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
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
    success_message = "Your profile has been succesfully created"


class MechanicUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
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
    success_message = "Your profile has been succesfully updated"


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
