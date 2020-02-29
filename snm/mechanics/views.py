"""Views."""
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, ListView,
                                  UpdateView)

from snm.carowners.models import CustomUser

from .forms import MechanicSignUpForm
from .models import Mechanic, Speciality


class MechanicSignUp(SuccessMessageMixin, CreateView):
    """Sign up view for all users."""

    model = CustomUser
    form_class = MechanicSignUpForm
    template_name = "registration/signup_form.html"
    success_message = "Successfully signed up, complete your profile"

    def get_context_data(self, **kwargs):
        """Get the user type."""
        kwargs["user_type"] = "mechanic"
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        """Define a valid form."""
        user = form.save()
        login(self.request, user)
        return redirect("mechanics:mech_create")


class MechanicListView(ListView):
    """List view of spareparts."""

    queryset = Mechanic.objects.all()
    context_object_name = "mechanics"


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

    def get_success_url(self):
        return reverse_lazy(
            "mechanics:mechanic", kwargs={"pk": self.object.pk}
        )


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

    def get_success_url(self):
        return reverse_lazy(
            "mechanics:mechanic", kwargs={"pk": self.object.pk}
        )


class MechanicDetailView(DetailView):
    """View a mechanics details."""

    model = Mechanic
    context_object_name = "mechanic"


class SearchResultsView(ListView):
    """Search view for specialities."""

    model = Mechanic
    template_name = "mechanics/search_results.html"

    def get_queryset(self):
        """Get filtered queryset."""
        query = self.request.GET.get("q")
        return Mechanic.objects.filter(Q(specialities__name__icontains=query))
