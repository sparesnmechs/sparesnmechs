"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.db.models import Q
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
from .filters import SparePartFilter
from django.shortcuts import render


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
        return reverse_lazy("sparedealers:listings")

    def form_valid(self, form):
        """Add the logged in user."""
        form.instance.dealer = self.request.user
        return super().form_valid(form)


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
        return reverse_lazy("sparedealers:listings")

    def form_valid(self, form):
        """Add the logged in user."""
        form.instance.dealer = self.request.user
        return super().form_valid(form)


class DealerListingsListView(LoginRequiredMixin, ListView):
    """A user can see their listings."""

    template_name = "listings.html"
    context_object_name = "listings"

    def get_queryset(self):
        """Filter by user."""
        return SparePart.objects.filter(dealer=self.request.user)


class SparePartDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = SparePart
    success_url = reverse_lazy('sparedealers:listings')


class SparePartDetailView(DetailView):
    """Detail view of spareparts."""

    model = SparePart
    context_object_name = "sparepart_detail"


class SparePartCategoryListView(ListView):
    """List view of spareparts."""

    queryset = SparePartCategory.objects.all()
    context_object_name = "categories"
    template_name = "index.html"


# # ==========Exterior category & subcategories==========
# class ExteriorSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Exterior")
#     queryset = category.part_categories.all()
#     context_object_name = "exteriors"
#     template_name = "spareparts/exterior/exterior.html"


# class TailLightsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Tail lights")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "tail_lights"
#     template_name = "spareparts/exterior/tail_lights.html"


# class SideMirrorsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Side mirrors")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "side_mirrors"
#     template_name = "spareparts/exterior/side_mirrors.html"


# class HoodListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Hoods")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "hoods"
#     template_name = "spareparts/exterior/hoods.html"


# class BumperListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(
#         name="Bumpers and Valances"
#     )
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "bumpers"
#     template_name = "spareparts/exterior/bumpers.html"


# class LEDLightsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="LED lights")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "led_lights"
#     template_name = "spareparts/exterior/LED_lights.html"


# class SignalLightsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Signal lights")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "signal_lights"
#     template_name = "spareparts/exterior/signal_lights.html"


# class DoorsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Doors")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "doors"
#     template_name = "spareparts/exterior/doors.html"


# class HeadlampsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Headlamps")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "headlamps"
#     template_name = "spareparts/exterior/headlamps.html"


# class NoseCutListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Nose cut")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "nose_cut"
#     template_name = "spareparts/exterior/nose_cut.html"


# class GrillesListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Grilles")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "grilles"
#     template_name = "spareparts/exterior/grilles.html"


# class FogLampsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Fog lamps")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "fog_lamps"
#     template_name = "spareparts/exterior/fog_lamps.html"


# # ==========Interior category & subcategories==========
# class InteriorSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Interior")
#     queryset = category.part_categories.all()
#     context_object_name = "interiors"
#     template_name = "spareparts/interior/interior.html"


# class FloorMatsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Floor mats")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "floor_mats"
#     template_name = "spareparts/interior/floor_mats.html"


# class CamerasListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Cameras")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "cameras"
#     template_name = "spareparts/interior/cameras.html"


# class SeatCoversListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Seat covers")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "seat_covers"
#     template_name = "spareparts/interior/seat_covers.html"


# class CoolingSystemsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Cooling systems")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "cooling_systems"
#     template_name = "spareparts/interior/cooling_systems.html"


# class TimingKitsListiew(ListView):
#     """Exterior spareparts."""

#     sub_category = SparePartSubCategory.objects.get(name="Timing kits")
#     queryset = sub_category.part_subcategories.all()
#     context_object_name = "timing_kits"
#     template_name = "spareparts/interior/timing_kits.html"


# # ==========Accessories category & subcategories==========
# class AccessoriesSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Accessories")
#     queryset = category.part_categories.all()
#     context_object_name = "accessories"
#     template_name = "spareparts/accessories.html"


# # ==========Audio category & subcategories==========
# class AudioSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Audio")  # Audio&Video
#     queryset = category.part_categories.all()
#     context_object_name = "audios"
#     template_name = "spareparts/audio_n_video.html"


# # ==========Electrical category & subcategories==========
# class ElectricalSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Electrical")
#     queryset = category.part_categories.all()
#     context_object_name = "electricals"
#     template_name = "spareparts/electrical.html"


# # ==========Engine category & subcategories==========
# class EngineSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Engine")
#     queryset = category.part_categories.all()
#     context_object_name = "engines"
#     template_name = "spareparts/engine.html"


# # ==========Performance category & subcategories==========
# class PerformanceSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Performance")
#     queryset = category.part_categories.all()
#     context_object_name = "performances"
#     template_name = "spareparts/performance.html"


# # ==========Suspsension category & subcategories==========
# class SuspensionSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Suspension")
#     queryset = category.part_categories.all()
#     context_object_name = "suspensions"
#     template_name = "spareparts/suspension.html"


# # ==========Transmission category & subcategories==========
# class TransmissionSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Transmission")
#     queryset = category.part_categories.all()
#     context_object_name = "transmissions"
#     template_name = "spareparts/transmission.html"


# # ==========Wheels category & subcategories==========
# class WheelsSparepartsListiew(ListView):
#     """Exterior spareparts."""

#     category = SparePartCategory.objects.get(name="Wheels")
#     queryset = category.part_categories.all()
#     context_object_name = "wheels"
#     template_name = "spareparts/wheels_n_tyres.html"


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


class SearchResultsView(ListView):
    """Search view for spareparts."""

    model = SparePart
    template_name = "spareparts/search_results.html"

    def get_queryset(self):
        """Get filtered queryset."""
        query = self.request.GET.get("q")
        return SparePart.objects.filter(
            Q(name__icontains=query)
            | Q(car_make__name__icontains=query)
            | Q(car_model__name__icontains=query)
            | Q(category__name__icontains=query)
            | Q(sub_category__name__icontains=query)
        )


def filtered_sparepart_list(request):
    f = SparePartFilter(request.GET, queryset=SparePart.objects.all())
    return render(request, "index.html", {"filter": f})
