"""Mechanic views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    UpdateView,
    DetailView,
)

from .models import Mechanic
from .forms import MechanicForm
from .filters import MechanicFilter
from django.shortcuts import render


def filtered_mechanic_list(request):
    f = MechanicFilter(request.GET, queryset=Mechanic.objects.all())
    return render(request, "mechanics/mechanic.html", {"filter": f})


class MechanicCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Create view for mechanics."""

    model = Mechanic
    form_class = MechanicForm
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Mechanic has been succesfully created"
    template_name = "mechanics/create_a_mechanic.html"

    def get_success_url(self):
        return reverse_lazy("mechanics:listings")

    def form_valid(self, form):
        """Add the logged in user."""
        form.instance.mechanic = self.request.user
        form.instance.first_name = self.request.user.first_name
        form.instance.last_name = self.request.user.last_name
        return super().form_valid(form)


class MechanicUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view for spare parts."""

    model = Mechanic
    form_class = MechanicForm
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your speciality has been succesfully updated"
    template_name = "mechanics/create_a_mechanic.html"

    def get_success_url(self):
        return reverse_lazy("mechanics:listings")

    def form_valid(self, form):
        """Add the logged in user."""
        form.instance.mechanic = self.request.user
        return super().form_valid(form)


class MechanicListingsListView(LoginRequiredMixin, ListView):
    """A user can see their listings."""

    template_name = "mechanics/mechanic_listings.html"
    context_object_name = "listings"

    def get_queryset(self):
        """Filter by user."""
        return Mechanic.objects.filter(mechanic=self.request.user)


class MechanicDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = Mechanic
    success_url = reverse_lazy("mechanics:listings")
    template_name = "mechanics/delete.html"


class SearchResultsView(ListView):
    """Search view for mechanics."""

    model = Mechanic
    template_name = "mechanics/search_results.html"

    def get_queryset(self):
        """Get filtered queryset."""
        query = self.request.GET.get("q")
        return Mechanic.objects.filter(
            Q(location__icontains=query)
            | Q(speciality__speciality__icontains=query)
            | Q(garage__icontains=query)
            | Q(car_make__name__icontains=query)
        )


class MechanicDetailView(DetailView):
    """Detail view of cechanics."""

    model = Mechanic
    template_name = "mechanics/details.html"


class BodyWorkListView(ListView):
    """View items in body works category."""

    queryset = Mechanic.objects.filter(speciality__speciality="Body work")
    template_name = "mechanics/body_work/body_work.html"


class ElectricalListView(ListView):
    """View items in electrical category."""

    queryset = Mechanic.objects.filter(speciality__speciality="Electrical")
    template_name = "mechanics/electrical/electrical.html"


class MechanicalListView(ListView):
    """View items in mechanical category."""

    queryset = Mechanic.objects.filter(speciality__speciality="Mechanical")
    template_name = "mechanics/mechanical/mechanical.html"
