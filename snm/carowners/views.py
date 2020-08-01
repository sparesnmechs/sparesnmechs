"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    TemplateView,
)

from .models import CarModel, CarOwner
from snm.sparedealers.forms import CustomUserCreationForm, CustomUserChangeForm


class SignUp(CreateView):
    """Sign up view for all users."""

    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class DetailsUpdate(UpdateView):
    """Change user details."""

    model = User
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("login")
    template_name = "registration/update.html"


class ContactUs(TemplateView):
    """Create a contact us page."""

    template_name = "contact_us.html"


class CarownerCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Create view for spare parts."""

    model = CarOwner
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "car_make",
        "car_model",
        "description",
    ]
    success_message = "Your profile has been succesfully created"

    def get_success_url(self):
        return reverse_lazy(
            "carowners:carowner", kwargs={"pk": self.object.pk}
        )


class CarownerUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view for spare parts."""

    model = CarOwner
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "car_make",
        "car_model",
        "description",
    ]
    success_message = "Your profile has been succesfully updated"

    def get_success_url(self):
        return reverse_lazy(
            "carowners:carowner", kwargs={"pk": self.object.pk}
        )


class OwnerDetailView(DetailView):
    """View a mechanics details."""

    model = CarOwner
    context_object_name = "carowner"


def get_carmodels(request):
    """Fetch car models."""
    car_make = request.GET.get("car_make", None)
    if not car_make:
        return HttpResponse(
            serializers.serialize("json", CarModel.objects.all()),
            content_type="application/json",
        )
    car_makes = CarModel.objects.filter(car_make=car_make)
    return HttpResponse(
        serializers.serialize("json", car_makes),
        content_type="application/json",
    )
