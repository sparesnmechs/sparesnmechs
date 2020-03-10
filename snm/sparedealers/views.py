"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import SparePart, SparePartCategory, SparePartSubCategory


class SparePartCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
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
        "first_name",
        "last_name",
        "phone_number",
        "region",
        "place",
        "store",
        "photo",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully created"
    template_name = "spareparts/sell_a_part.html"

    def get_success_url(self):
        return reverse_lazy(
            "sparedealers:update", kwargs={"pk": self.object.pk}
        )


class SparePartUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
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
        "first_name",
        "last_name",
        "phone_number",
        "region",
        "place",
        "store",
        "photo",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully updated"
    template_name = "spareparts/update_a_part.html"

    def get_success_url(self):
        return reverse_lazy("sparedealers:sparepart-list")


class SparePartDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = SparePart
    login_url = "login"
    redirect_field_name = "redirect_to"


class SparePartListView(ListView):
    """List view of spareparts."""

    queryset = SparePart.objects.all()
    context_object_name = "spareparts"
    template_name = "index.html"


class SparePartDetailView(DetailView):
    """Detail view of spareparts."""

    model = SparePart
    context_object_name = "sparepart_detail"


class SparePartCategoryListView(ListView):
    """List view of spareparts."""

    queryset = SparePartCategory.objects.all()
    context_object_name = "categories"
    template_name = "index.html"


class ExteriorSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    queryset = category.part_categories.all()
    context_object_name = "exteriors"
    template_name = "spareparts/exterior.html"


class InteriorSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    queryset = category.part_categories.all()
    context_object_name = "interiors"
    template_name = "spareparts/interior.html"


class AccessoriesSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    queryset = category.part_categories.all()
    context_object_name = "accessories"
    template_name = "spareparts/accessories.html"


class AudioSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(id=2)  # Audio&Video
    queryset = category.part_categories.all()
    context_object_name = "audios"
    template_name = "spareparts/audio_n_video.html"


class ElectricalSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    queryset = category.part_categories.all()
    context_object_name = "electricals"
    template_name = "spareparts/electrical.html"


class EngineSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    queryset = category.part_categories.all()
    context_object_name = "engines"
    template_name = "spareparts/engine.html"


class PerformanceSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    queryset = category.part_categories.all()
    context_object_name = "performances"
    template_name = "spareparts/performance.html"


class SuspensionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    queryset = category.part_categories.all()
    context_object_name = "suspensions"
    template_name = "spareparts/suspension.html"


class TransmissionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Transmission")
    queryset = category.part_categories.all()
    context_object_name = "transmissions"
    template_name = "spareparts/transmission.html"


class WheelsSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(id=10)
    queryset = category.part_categories.all()
    context_object_name = "wheels"
    template_name = "spareparts/wheels_n_tyres.html"


def get_subcategories(request):
    """Get subcategories based on their categories."""
    category = request.GET.get("category", None)
    if not category:
        return HttpResponse(
            serializers.serialize("json", SparePartSubCategory.objects.all()),
            content_type="application/json",
        )
    sub_categories = SparePartSubCategory.objects.filter(category=category)
    return HttpResponse(
        serializers.serialize("json", sub_categories),
        content_type="application/json",
    )
