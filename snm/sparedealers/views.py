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

    category = SparePartCategory.objects.get(name="Exterior")
    queryset = category.part_categories.all()
    template_name = "spareparts/exterior/exterior.html"


class PanelsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Panels")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/panels.html"


class WindowsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Windows")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/windows.html"


class WindowLouversListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Window louvers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/window_louvers.html"


class FendersListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Fender flares")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/fender_flares.html"


class TrunkLidsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Trunk lids")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/trunk_lids.html"


class SpoilersListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Spoilers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/spoilers.html"


class LightCoversListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Light covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/light_covers.html"


class EyelidsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Eyelids")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/eye_lids.html"


class RoofsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Roofs")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/roofs.html"


class FendorsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Fendors")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/fendors.html"


class BodyKitListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Body kit")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/body_kit.html"


class CanardsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Canards")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/canards.html"


class BumperLipsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Bumper lips")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/bumper_lips.html"


class CargoLinersListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Cargo liners")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/cargo_liners.html"


class SideMirrorsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Side mirrors")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/side_mirrors.html"


class HoodListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Hoods")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/hoods.html"


class BumperListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(
        name="Bumpers and Valances"
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/bumpers.html"


class DoorsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Doors")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/doors.html"


class NoseCutListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Nose cut")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/nose_cut.html"


class GrillesListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Grilles")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/exterior/grilles.html"


# ==========Interior category & subcategories==========
class InteriorSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Interior")
    queryset = category.part_categories.all()
    template_name = "spareparts/interior/interior.html"


class ShiftKnobsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Shift knobs")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/shift_knobs.html"


class DashCoversListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Dash covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/dash_covers.html"


class SunShadesListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Sun shades")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/sun_shades.html"


class SteeringWheelsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Steering wheels")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/interior/steering_wheels.html"


# ==========Accessories category & subcategories==========
class AccessoriesSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Accessories")
    queryset = category.part_categories.all()
    template_name = "spareparts/accessories/accessories.html"


class DashKitsListiew(ListView):
    """Exterior spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Dash kits")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/dash_kits.html"


class SeatCoversListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Seat covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/seat_covers.html"


class SteeringCoversListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Steering covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/steering_covers.html"


class CamerasListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Cameras")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/cameras.html"


class TICListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(
        name="Tire inflator compressor"
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/tire_inflator_compressor.html"


class RDListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Radar detectors")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/radar_detectors.html"


class MCListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Mounts and chargers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/mounts_and_chargers.html"


class GPSListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Gps systems")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/gps_systems.html"


class FloorMatsListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Floor mats")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/floor_mats.html"


class STCoverListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Spare tire cover")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/spare_tire_covers.html"


class LNLListiew(ListView):
    """accessories spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Lock nuts and locks")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/accessories/lock_nuts_and_locks.html"


# ==========Audio category & subcategories==========
class AudioSparepartsListiew(ListView):
    """Audio spareparts."""

    category = SparePartCategory.objects.get(name="Audio")  # Audio&Video
    queryset = category.part_categories.all()
    template_name = "spareparts/audio/audio_n_video.html"


class SubWooferListiew(ListView):
    """Audio spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Subwoofer")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/subwoofers.html"


class SpeakersListiew(ListView):
    """Audio spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Speakers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/speakers.html"


class EqualizerListiew(ListView):
    """Audio spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Equalizer")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/equalizers.html"


class StereosListiew(ListView):
    """Audio spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Stereo")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/stereos.html"


class AmplifiersListiew(ListView):
    """Audio spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Amplifiers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/audio/amplifiers.html"


# ==========Electrical category & subcategories==========
class ElectricalSparepartsListiew(ListView):
    """Electrical spareparts."""

    category = SparePartCategory.objects.get(name="Electrical")
    queryset = category.part_categories.all()
    template_name = "spareparts/electrical/electrical.html"


class HeadLampsListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Headlamps")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/headlamps.html"


class CUListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Control units")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/control_units.html"


class ARSListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(
        name="Alarm and remote start"
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/ars.html"


class FogLampsListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Fog lamps")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/fog_lamps.html"


class BatteryListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Battery")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/battery.html"


class CarBulbsListiew(ListView):
    """Electrical spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Car bulbs")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/electrical/car_bulbs.html"


# ==========Engine category & subcategories==========
class EngineSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Engine")
    queryset = category.part_categories.all()
    template_name = "spareparts/engine/engine.html"


class EngineMountsListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Engine mounts")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_mounts.html"


class TKListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Timing kits")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/timing_kits.html"


class TensionersListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Tensioners")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/tensioners.html"


class ExhaustsListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Exhausts")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/exhausts.html"


class ISListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Ignition systems")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/ignition_systems.html"


class FSListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Fuel system")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/fuel_systems.html"


class ECListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Engine components")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_components.html"


class EngineCoversListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Engine covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engine_covers.html"


class EnginesListiew(ListView):
    """Engine spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Engine")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/engine/engines.html"


# ==========Performance category & subcategories==========
class PerformanceSparepartsListiew(ListView):
    """Performance spareparts."""

    category = SparePartCategory.objects.get(name="Performance")
    queryset = category.part_categories.all()
    template_name = "spareparts/performance/performance.html"


class CoilOversListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Coilovers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/coilovers.html"


class RTHListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Racing tow hooks")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/racing_tow_hooks.html"


class DiffusersListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Diffuser")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/diffusers.html"


class RacingGearsListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Racing gear")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/racing_gears.html"


class PCListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Performance chips")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/performance_chips.html"


class CSListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Cooling systems")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/cooling_systems.html"


class AISListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Air intake systems")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/air_intake_systems.html"


class PedalsListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Pedals")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/pedals.html"


class CustomGaugesListiew(ListView):
    """Performance spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Custom gauges")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/performance/custom_gauges.html"


# ==========Suspsension category & subcategories==========
class SuspensionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Suspension")
    queryset = category.part_categories.all()
    template_name = "spareparts/suspensions/suspension.html"


class DAAListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Driveline and axles")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/driveline_and_axles.html"


class SpacerListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Spacer")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/spacers.html"


class ShockAbsListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Shock absorbers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/shock_absorbers.html"


class ECUListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Suspension ecu")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/suspensions/ecus.html"


# ==========Transmission category & subcategories==========
class TransmissionSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Transmission")
    queryset = category.part_categories.all()
    template_name = "spareparts/transmissions/transmission.html"


class TransMountListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Transmission mounts")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/transmissions_mounts.html"


class TransComponentsListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(
        name="Transmission components"
    )
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/transmission_components.html"


class TransListiew(ListView):
    """Suspensions spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Transmission")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/transmissions/trans.html"


# ==========Wheels category & subcategories==========
class WheelsSparepartsListiew(ListView):
    """Exterior spareparts."""

    category = SparePartCategory.objects.get(name="Wheels")
    queryset = category.part_categories.all()
    template_name = "spareparts/wheels_and_tires/wheels.html"


class TPMSListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Tpms sensor")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/tpms_sensors.html"


class WheelSpacerListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Wheel spacer")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/wheel_spacers.html"


class TiresListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Tires")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/tires.html"


class RimsListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Rims")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/rims.html"


class WheelCoversListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Wheel covers")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/wheel_covers.html"


class LockingNutsListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Locking nuts")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/locking_nuts.html"


class CenterCapsListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Center caps")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/center_caps.html"


class BCCListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Brake caliper cover")
    queryset = sub_category.part_subcategories.all()
    template_name = "spareparts/wheels_and_tires/brake_calipers_covers.html"


class BRListiew(ListView):
    """Wheels and tyres spareparts."""

    sub_category = SparePartSubCategory.objects.get(name="Brakes and rotors")
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
