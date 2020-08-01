"""Sparedealers app urls."""
from django.urls import path

from . import views

app_name = "sparedealers"
urlpatterns = [
    path("", views.filtered_sparepart_list, name="sparepart-list",),
    path(
        "sparepart/create", views.SparePartCreateView.as_view(), name="create",
    ),
    path(
        "sparepart/update/<int:pk>",
        views.SparePartUpdateView.as_view(),
        name="update",
    ),
    path(
        "spareparts/subcategories",
        views.get_subcategories,
        name="get_subcategories",
    ),
    path(
        "sparepart/<int:pk>",
        views.SparePartDetailView.as_view(),
        name="sparepart_detail",
    ),
    path(
        "sparepart/category/",
        views.SparePartCategoryListView.as_view(),
        name="category",
    ),
    path(
        "listings/", views.DealerListingsListView.as_view(), name="listings",
    ),
    path(
        "delete/<int:pk>", views.SparePartDeleteView.as_view(), name="delete",
    ),
    path("requests/", views.EmailCreateView.as_view(), name="requests",),
    path("profile/", views.ProfileView.as_view(), name="profile",),
    # ==========Exterior category & subcategories==========
    # path(
    #     "sparepart/category/exterior/",
    #     views.ExteriorSparepartsListiew.as_view(),
    #     name="exterior",
    # ),
    # path(
    #     "sparepart/category/exterior/side_mirrors/",
    #     views.SideMirrorsListiew.as_view(),
    #     name="side_mirrors",
    # ),
    # path(
    #     "sparepart/category/exterior/panels/",
    #     views.PanelsListiew.as_view(),
    #     name="panels",
    # ),
    # path(
    #     "sparepart/category/exterior/windows/",
    #     views.WindowsListiew.as_view(),
    #     name="windows",
    # ),
    # path(
    #     "sparepart/category/exterior/window_louvers/",
    #     views.WindowLouversListiew.as_view(),
    #     name="window_louvers",
    # ),
    # path(
    #     "sparepart/category/exterior/fenders/",
    #     views.FendersListiew.as_view(),
    #     name="fenders",
    # ),
    # path(
    #     "sparepart/category/exterior/trunk_lids/",
    #     views.TrunkLidsListiew.as_view(),
    #     name="trunk_lids",
    # ),
    # path(
    #     "sparepart/category/exterior/spoilers/",
    #     views.SpoilersListiew.as_view(),
    #     name="spoilers",
    # ),
    # path(
    #     "sparepart/category/exterior/light_covers/",
    #     views.LightCoversListiew.as_view(),
    #     name="light_covers",
    # ),
    # path(
    #     "sparepart/category/exterior/eye_lids/",
    #     views.EyelidsListiew.as_view(),
    #     name="eye_lids",
    # ),
    # path(
    #     "sparepart/category/exterior/roofs/",
    #     views.RoofsListiew.as_view(),
    #     name="roofs",
    # ),
    # path(
    #     "sparepart/category/exterior/fendors/",
    #     views.FendorsListiew.as_view(),
    #     name="fendors",
    # ),
    # path(
    #     "sparepart/category/exterior/body_kit/",
    #     views.BodyKitListiew.as_view(),
    #     name="body_kit",
    # ),
    # path(
    #     "sparepart/category/exterior/canards/",
    #     views.CanardsListiew.as_view(),
    #     name="canards",
    # ),
    # path(
    #     "sparepart/category/exterior/bumper_lips/",
    #     views.BumperLipsListiew.as_view(),
    #     name="bumper_lips",
    # ),
    # path(
    #     "sparepart/category/exterior/cargo_liners/",
    #     views.CargoLinersListiew.as_view(),
    #     name="cargo_liners",
    # ),
    # path(
    #     "sparepart/category/exterior/hoods/",
    #     views.HoodListiew.as_view(),
    #     name="hoods",
    # ),
    # path(
    #     "sparepart/category/exterior/bumpers_and_valances/",
    #     views.BumperListiew.as_view(),
    #     name="bumpers_and_valances",
    # ),
    # path(
    #     "sparepart/category/exterior/doors/",
    #     views.DoorsListiew.as_view(),
    #     name="doors",
    # ),
    # path(
    #     "sparepart/category/exterior/nose_cut/",
    #     views.NoseCutListiew.as_view(),
    #     name="nose_cut",
    # ),
    # path(
    #     "sparepart/category/exterior/grilles/",
    #     views.GrillesListiew.as_view(),
    #     name="grilles",
    # ),
    # # ==========Interior category & subcategories==========
    # path(
    #     "sparepart/category/interior/",
    #     views.InteriorSparepartsListiew.as_view(),
    #     name="interior",
    # ),
    # path(
    #     "sparepart/category/interior/shift_knobs/",
    #     views.ShiftKnobsListiew.as_view(),
    #     name="shift_knobs",
    # ),
    # path(
    #     "sparepart/category/interior/dash_covers/",
    #     views.DashCoversListiew.as_view(),
    #     name="dash_covers",
    # ),
    # path(
    #     "sparepart/category/interior/sun_shades/",
    #     views.SunShadesListiew.as_view(),
    #     name="sun_shades",
    # ),
    # path(
    #     "sparepart/category/interior/steering_wheels/",
    #     views.SteeringWheelsListiew.as_view(),
    #     name="steering_wheels",
    # ),
    # # ==========Accessories category & subcategories==========
    # path(
    #     "sparepart/category/accessories/",
    #     views.AccessoriesSparepartsListiew.as_view(),
    #     name="accessories",
    # ),
    # path(
    #     "sparepart/category/accessories/dash_kits/",
    #     views.DashKitsListiew.as_view(),
    #     name="dash_kits",
    # ),
    # path(
    #     "sparepart/category/accessories/seat_covers/",
    #     views.SeatCoversListiew.as_view(),
    #     name="seat_covers",
    # ),
    # path(
    #     "sparepart/category/accessories/steering_covers/",
    #     views.SteeringCoversListiew.as_view(),
    #     name="steering_covers",
    # ),
    # path(
    #     "sparepart/category/accessories/cameras/",
    #     views.CamerasListiew.as_view(),
    #     name="cameras",
    # ),
    # path(
    #     "sparepart/category/accessories/tire_inflator_compressor/",
    #     views.TICListiew.as_view(),
    #     name="tire_inflator_compressor",
    # ),
    # path(
    #     "sparepart/category/accessories/radar_detectors/",
    #     views.RDListiew.as_view(),
    #     name="radar_detectors",
    # ),
    # path(
    #     "sparepart/category/accessories/mounts_and_chargers/",
    #     views.MCListiew.as_view(),
    #     name="mounts_and_chargers",
    # ),
    # path(
    #     "sparepart/category/accessories/gps_systems/",
    #     views.GPSListiew.as_view(),
    #     name="gps_systems",
    # ),
    # path(
    #     "sparepart/category/accessories/floor_mats/",
    #     views.FloorMatsListiew.as_view(),
    #     name="floor_mats",
    # ),
    # path(
    #     "sparepart/category/accessories/spare_tire_covers/",
    #     views.STCoverListiew.as_view(),
    #     name="spare_tire_covers",
    # ),
    # path(
    #     "sparepart/category/accessories/lock_nuts_and_locks/",
    #     views.LNLListiew.as_view(),
    #     name="lock_nuts_and_locks",
    # ),
    # # ==========Audio & Videos category & subcategories==========
    # path(
    #     "sparepart/category/audios/",
    #     views.AudioSparepartsListiew.as_view(),
    #     name="audio",
    # ),
    # path(
    #     "sparepart/category/audios/subwoofers",
    #     views.SubWooferListiew.as_view(),
    #     name="subwoofers",
    # ),
    # path(
    #     "sparepart/category/audios/speakers",
    #     views.SpeakersListiew.as_view(),
    #     name="speakers",
    # ),
    # path(
    #     "sparepart/category/audios/equalizers",
    #     views.EqualizerListiew.as_view(),
    #     name="equalizers",
    # ),
    # path(
    #     "sparepart/category/audios/stereos",
    #     views.StereosListiew.as_view(),
    #     name="stereos",
    # ),
    # path(
    #     "sparepart/category/audios/amplifiers",
    #     views.AmplifiersListiew.as_view(),
    #     name="amplifiers",
    # ),
    # # ==========Engine category & subcategories==========
    # path(
    #     "sparepart/category/engine/",
    #     views.EngineSparepartsListiew.as_view(),
    #     name="engine",
    # ),
    # path(
    #     "sparepart/category/engine/engines",
    #     views.EnginesListiew.as_view(),
    #     name="engines",
    # ),
    # path(
    #     "sparepart/category/engine/engine_mounts",
    #     views.EngineMountsListiew.as_view(),
    #     name="engine_mounts",
    # ),
    # path(
    #     "sparepart/category/engine/timing_kits",
    #     views.TKListiew.as_view(),
    #     name="timing_kits",
    # ),
    # path(
    #     "sparepart/category/engine/tensioners",
    #     views.TensionersListiew.as_view(),
    #     name="tensioners",
    # ),
    # path(
    #     "sparepart/category/engine/exhausts",
    #     views.ExhaustsListiew.as_view(),
    #     name="exhausts",
    # ),
    # path(
    #     "sparepart/category/engine/ignition_systems",
    #     views.ISListiew.as_view(),
    #     name="ignition_systems",
    # ),
    # path(
    #     "sparepart/category/engine/fuel_systems",
    #     views.FSListiew.as_view(),
    #     name="fuel_systems",
    # ),
    # path(
    #     "sparepart/category/engine/engine_components",
    #     views.ECListiew.as_view(),
    #     name="engine_components",
    # ),
    # path(
    #     "sparepart/category/engine/engine_covers",
    #     views.EngineCoversListiew.as_view(),
    #     name="engine_covers",
    # ),
    # # ==========Performance category & subcategories==========
    # path(
    #     "sparepart/category/performance/",
    #     views.PerformanceSparepartsListiew.as_view(),
    #     name="performance",
    # ),
    # path(
    #     "sparepart/category/performance/coilovers/",
    #     views.CoilOversListiew.as_view(),
    #     name="coilovers",
    # ),
    # path(
    #     "sparepart/category/performance/racing_tow_hooks/",
    #     views.RTHListiew.as_view(),
    #     name="racing_tow_hooks",
    # ),
    # path(
    #     "sparepart/category/performance/diffusers/",
    #     views.DiffusersListiew.as_view(),
    #     name="diffusers",
    # ),
    # path(
    #     "sparepart/category/performance/racing_gears/",
    #     views.RacingGearsListiew.as_view(),
    #     name="racing_gears",
    # ),
    # path(
    #     "sparepart/category/performance/performance_chips/",
    #     views.PCListiew.as_view(),
    #     name="performance_chips",
    # ),
    # path(
    #     "sparepart/category/performance/cooling_systems/",
    #     views.CSListiew.as_view(),
    #     name="cooling_systems",
    # ),
    # path(
    #     "sparepart/category/performance/air_intake_systems/",
    #     views.AISListiew.as_view(),
    #     name="air_intake_systems",
    # ),
    # path(
    #     "sparepart/category/performance/pedals/",
    #     views.PedalsListiew.as_view(),
    #     name="pedals",
    # ),
    # path(
    #     "sparepart/category/performance/custom_gauges/",
    #     views.CustomGaugesListiew.as_view(),
    #     name="custom_gauges",
    # ),
    # # ==========Suspension category & subcategories==========
    # path(
    #     "sparepart/category/suspension/",
    #     views.SuspensionSparepartsListiew.as_view(),
    #     name="suspension",
    # ),
    # path(
    #     "sparepart/category/suspension/driveline_and_axles/",
    #     views.DAAListiew.as_view(),
    #     name="driveline_and_axles",
    # ),
    # path(
    #     "sparepart/category/suspension/spacers/",
    #     views.SpacerListiew.as_view(),
    #     name="spacers",
    # ),
    # path(
    #     "sparepart/category/suspension/shock_absorbers/",
    #     views.ShockAbsListiew.as_view(),
    #     name="shock_absorbers",
    # ),
    # path(
    #     "sparepart/category/suspension/ecus/",
    #     views.ECUListiew.as_view(),
    #     name="ecus",
    # ),
    # # ==========Transmission category & subcategories==========
    # path(
    #     "sparepart/category/transmission/",
    #     views.TransmissionSparepartsListiew.as_view(),
    #     name="transmission",
    # ),
    # path(
    #     "sparepart/category/transmission/transmission_mounts/",
    #     views.TransMountListiew.as_view(),
    #     name="transmission_mounts",
    # ),
    # path(
    #     "sparepart/category/transmission/transmission_components/",
    #     views.TransComponentsListiew.as_view(),
    #     name="transmission_components",
    # ),
    # path(
    #     "sparepart/category/transmission/transmissions/",
    #     views.TransListiew.as_view(),
    #     name="trans",
    # ),
    # # ==========Wheels & Tyres category & subcategories==========
    # path(
    #     "sparepart/category/wheels/",
    #     views.WheelsSparepartsListiew.as_view(),
    #     name="wheels",
    # ),
    # path(
    #     "sparepart/category/wheels/tires",
    #     views.TiresListiew.as_view(),
    #     name="tires",
    # ),
    # path(
    #     "sparepart/category/wheels/rims",
    #     views.RimsListiew.as_view(),
    #     name="rims",
    # ),
    # path(
    #     "sparepart/category/wheels/wheel_spacers",
    #     views.WheelSpacerListiew.as_view(),
    #     name="wheel_spacers",
    # ),
    # path(
    #     "sparepart/category/wheels/wheel_covers",
    #     views.WheelCoversListiew.as_view(),
    #     name="wheel_covers",
    # ),
    # path(
    #     "sparepart/category/wheels/locking_nuts",
    #     views.LockingNutsListiew.as_view(),
    #     name="locking_nuts",
    # ),
    # path(
    #     "sparepart/category/wheels/center_caps",
    #     views.CenterCapsListiew.as_view(),
    #     name="center_caps",
    # ),
    # path(
    #     "sparepart/category/wheels/brake_caliper_covers",
    #     views.BCCListiew.as_view(),
    #     name="brake_caliper_covers",
    # ),
    # path(
    #     "sparepart/category/wheels/brakes_and_rotors",
    #     views.BRListiew.as_view(),
    #     name="brakes_and_rotors",
    # ),
    # # ==========Electrical category & subcategories==========
    # path(
    #     "sparepart/category/electrical/",
    #     views.ElectricalSparepartsListiew.as_view(),
    #     name="electrical",
    # ),
    # path(
    #     "sparepart/category/electrical/headlamps",
    #     views.HeadLampsListiew.as_view(),
    #     name="headlamps",
    # ),
    # path(
    #     "sparepart/category/electrical/control_units",
    #     views.CUListiew.as_view(),
    #     name="control_units",
    # ),
    # path(
    #     "sparepart/category/electrical/alarm_and_remote_start",
    #     views.ARSListiew.as_view(),
    #     name="alarm_and_remote_start",
    # ),
    # path(
    #     "sparepart/category/electrical/fog_lamps",
    #     views.FogLampsListiew.as_view(),
    #     name="fog_lamps",
    # ),
    # path(
    #     "sparepart/category/electrical/car_bulbs",
    #     views.CarBulbsListiew.as_view(),
    #     name="car_bulbs",
    # ),
    # path(
    #     "sparepart/category/electrical/battery",
    #     views.BatteryListiew.as_view(),
    #     name="battery",
    # ),
    path(
        "spareparts/search/",
        views.SearchResultsView.as_view(),
        name="search_results",
    ),
]
