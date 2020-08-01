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
    FormView,
    TemplateView,
)

from .models import SparePart, SparePartCategory, SparePartSubCategory
from .filters import SparePartFilter
from django.shortcuts import render
from .forms import EmailForm, SellPartForm


class SparePartCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Create view for spare parts."""

    model = SparePart
    form_class = SellPartForm
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully created"
    template_name = "spareparts/sell_a_part.html"

    def get_success_url(self):
        return reverse_lazy("sparedealers:listings")

    def form_valid(self, form):
        """Add the logged in user."""
        form.instance.dealer = self.request.user
        form.instance.first_name = self.request.user.first_name
        form.instance.last_name = self.request.user.last_name
        return super(SparePartCreateView, self).form_valid(form)


class SparePartUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view for spare parts."""

    model = SparePart
    form_class = SellPartForm
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully updated"
    template_name = "spareparts/sell_a_part.html"

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
    success_url = reverse_lazy("sparedealers:listings")


class SparePartDetailView(DetailView):
    """Detail view of spareparts."""

    model = SparePart
    template_name = "details.html"


class SparePartCategoryListView(ListView):
    """List view of spareparts."""

    queryset = SparePartCategory.objects.all()
    context_object_name = "categories"
    template_name = "index.html"


class EmailCreateView(SuccessMessageMixin, FormView):
    """Create email view."""

    template_name = "requests.html"
    form_class = EmailForm
    success_url = "/"
    success_message = "Your email has been sent"

    def form_valid(self, form):
        """Send email if form is valid."""
        form.send_email()
        return super().form_valid(form)


class ProfileView(TemplateView):
    """Profile view."""

    template_name = "registration/profile.html"


# ==========Exterior category & subcategories==========
class ExteriorSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Exterior")
    queryset = category.part_categories.all()
    template_name = "spareparts/exterior/exterior.html"


class PanelsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Panels", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/panels.html"


class WindowsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Windows", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/windows.html"


class WindowLouversListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Window louvers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/window_louvers.html"


class FendersListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Fender flares", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/fender_flares.html"


class TrunkLidsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Trunk lids", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/trunk_lids.html"


class SpoilersListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Spoilers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/spoilers.html"


class LightCoversListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Light covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/light_covers.html"


class EyelidsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Eyelids", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/eye_lids.html"


class RoofsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Roofs", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/roofs.html"


class FendorsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Fendors", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/fendors.html"


class BodyKitListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Body kit", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/body_kit.html"


class CanardsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Canards", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/canards.html"


class BumperLipsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Bumper lips", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/bumper_lips.html"


class CargoLinersListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Cargo liners", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/cargo_liners.html"


class SideMirrorsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Side mirrors", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/side_mirrors.html"


class HoodListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Hoods", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/hoods.html"


class BumperListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Bumpers and Valances", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/bumpers.html"


class DoorsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Doors", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/doors.html"


class NoseCutListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Nose cut", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/nose_cut.html"


class GrillesListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Exterior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Grilles", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/grilles.html"


# ==========Interior category & subcategories==========
class InteriorSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Interior")
    queryset = category.part_categories.all()
    template_name = "spareparts/interior/interior.html"


class ShiftKnobsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Shift knobs", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/shift_knobs.html"


class DashCoversListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Dash covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/dash_covers.html"


class SunShadesListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Sun shades", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/sun_shades.html"


class SteeringWheelsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Steering wheels", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/steering_wheels.html"


# ==========Accessories category & subcategories==========
class AccessoriesSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Accessories")
    queryset = category.part_categories.all()
    template_name = "spareparts/accessories/accessories.html"


class DashKitsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Dash kits", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/dash_kits.html"


class SeatCoversListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Seat covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/seat_covers.html"


class SteeringCoversListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Steering covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/steering_covers.html"


class CamerasListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Cameras", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/cameras.html"


class TICListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Tire inflator compressor", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/tire_inflator_compressor.html"


class RDListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Radar detectors", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/radar_detectors.html"


class MCListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Mounts and chargers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/mounts_and_chargers.html"


class GPSListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Gps systems", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/gps_systems.html"


class FloorMatsListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Floor mats", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/floor_mats.html"


class STCoverListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Spare tire cover", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/spare_tire_covers.html"


class LNLListiew(ListView):
    """accessories spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Lock nuts and locks", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/lock_nuts_and_locks.html"


# ==========Audio category & subcategories==========
class AudioSparepartsListiew(ListView):
    """Audio spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(
        name="Audio"
    )  # Audio&Video
    queryset = category.part_categories.all()
    template_name = "spareparts/audio/audio_n_video.html"


class SubWooferListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Subwoofer", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/subwoofers.html"


class SpeakersListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Speakers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/speakers.html"


class EqualizerListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Equalizer", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/equalizers.html"


class StereosListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Stereo", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/stereos.html"


class AmplifiersListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Amplifiers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/amplifiers.html"


# ==========Electrical category & subcategories==========
class ElectricalSparepartsListiew(ListView):
    """Electrical spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Electrical")
    queryset = category.part_categories.all()
    template_name = "spareparts/electrical/electrical.html"


class HeadLampsListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Headlamps", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/headlamps.html"


class CUListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Control units", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/control_units.html"


class ARSListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Alarm and remote start", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/ars.html"


class FogLampsListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Fog lamps", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/fog_lamps.html"


class BatteryListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Battery", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/battery.html"


class CarBulbsListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Car bulbs", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/car_bulbs.html"


# ==========Engine category & subcategories==========
class EngineSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Engine")
    queryset = category.part_categories.all()
    template_name = "spareparts/engine/engine.html"


class EngineMountsListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Engine mounts", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_mounts.html"


class TKListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Timing kits", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/timing_kits.html"


class TensionersListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Tensioners", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/tensioners.html"


class ExhaustsListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Exhausts", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/exhausts.html"


class ISListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Ignition systems", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/ignition_systems.html"


class FSListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Fuel system", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/fuel_systems.html"


class ECListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Engine components", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_components.html"


class EngineCoversListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Engine covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_covers.html"


class EnginesListiew(ListView):
    """Engine spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Engine", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engines.html"


# ==========Performance category & subcategories==========
class PerformanceSparepartsListiew(ListView):
    """Performance spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Performance")
    queryset = category.part_categories.all()
    template_name = "spareparts/performance/performance.html"


class CoilOversListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Coilovers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/coilovers.html"


class RTHListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Racing tow hooks", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/racing_tow_hooks.html"


class DiffusersListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Diffuser", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/diffusers.html"


class RacingGearsListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Racing gear", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/racing_gears.html"


class PCListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Performance chips", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/performance_chips.html"


class CSListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Cooling systems", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/cooling_systems.html"


class AISListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Air intake systems", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/air_intake_systems.html"


class PedalsListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Pedals", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/pedals.html"


class CustomGaugesListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Custom gauges", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/custom_gauges.html"


# ==========Suspsension category & subcategories==========
class SuspensionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Suspension")
    queryset = category.part_categories.all()
    template_name = "spareparts/suspensions/suspension.html"


class DAAListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Driveline and axles", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/driveline_and_axles.html"


class SpacerListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Spacer", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/spacers.html"


class ShockAbsListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Shock absorbers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/shock_absorbers.html"


class ECUListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Suspension ecu", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/ecus.html"


# ==========Transmission category & subcategories==========
class TransmissionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Transmission")
    queryset = category.part_categories.all()
    template_name = "spareparts/transmissions/transmission.html"


class TransMountListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Transmission")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Transmission mounts", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/transmissions_mounts.html"


class TransComponentsListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Transmission")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Transmission components", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/transmission_components.html"


class TransListiew(ListView):
    """Suspensions spareparts."""

    category = SparePartCategory.objects.get(name="Transmission")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Transmission", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/trans.html"


# ==========Wheels category & subcategories==========
class WheelsSparepartsListiew(ListView):
    """Exterior spareparts."""

    category, _ = SparePartCategory.objects.get_or_create(name="Wheels")
    queryset = category.part_categories.all()
    template_name = "spareparts/wheels_and_tires/wheels.html"


class TPMSListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Tpms sensor", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/tpms_sensors.html"


class WheelSpacerListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Wheel spacer", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/wheel_spacers.html"


class TiresListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Tires", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/tires.html"


class RimsListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Rims", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/rims.html"


class WheelCoversListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Wheel covers", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/wheel_covers.html"


class LockingNutsListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Locking nuts", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/locking_nuts.html"


class CenterCapsListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Center caps", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/center_caps.html"


class BCCListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Brake caliper cover", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/brake_calipers_covers.html"


class BRListiew(ListView):
    """Wheels and tyres spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    sub_category, _ = SparePartSubCategory.objects.get_or_create(
        name="Brakes and rotors", category=category
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/brakes_and_rotors.html"


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
