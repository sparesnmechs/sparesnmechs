"""Mechanic views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from .models import Speciality


class SpecialityListView(ListView):
    """List view of spareparts."""

    queryset = Speciality.objects.all()
    context_object_name = "specialities"
    template_name = "specialities/speciality.html"


class SpecialityCreateView(
    SuccessMessageMixin, LoginRequiredMixin, CreateView
):
    """Create view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
        "first_name",
        "last_name",
        "phone_number",
        "store",
        "photo",
        "region",
        "place",
        "price",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your speciality has been succesfully created"
    template_name = "specialities/sell_a_speciality.html"

    def get_success_url(self):
        return reverse_lazy("mechanics:update", kwargs={"pk": self.object.pk})


class SpecialityUpdateView(
    SuccessMessageMixin, LoginRequiredMixin, UpdateView
):
    """Update view for spare parts."""

    model = Speciality
    fields = [
        "name",
        "description",
        "car_make",
        "first_name",
        "last_name",
        "phone_number",
        "store",
        "photo",
        "region",
        "place",
        "price",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your speciality has been succesfully updated"
    template_name = "specialities/sell_a_speciality.html"
    template_name = "specialities/update_a_speciality.html"

    def get_success_url(self):
        return reverse_lazy("mechanics:speciality")


class SpecialityDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = Speciality
    login_url = "login"
    redirect_field_name = "redirect_to"


class SearchResultsView(ListView):
    """Search view for specialities."""

    model = Speciality
    template_name = "specialities/search_results.html"

    def get_queryset(self):
        """Get filtered queryset."""
        query = self.request.GET.get("q")
        return Speciality.objects.filter(
            Q(name__icontains=query) | Q(car_make__name__icontains=query)
        )
