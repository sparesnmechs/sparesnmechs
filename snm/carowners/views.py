"""Views."""
from django.contrib.auth.forms import UserCreationForm
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from .models import CarModel, CarOwner


class SignUp(CreateView):
    """Sign up view for all users."""

    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class CarownerCreateView(CreateView):
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


class CarownerUpdateView(UpdateView):
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


def get_carmodels(request):
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
