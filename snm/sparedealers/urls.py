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
        "listings/",
        views.DealerListingsListView.as_view(),
        name="listings",
    ),
    path(
        "delete/<int:pk>",
        views.SparePartDeleteView.as_view(),
        name="delete",
    ),
    # # ==========Exterior category & subcategories==========
    # path(
    #     "sparepart/category/exterior/",
    #     views.ExteriorSparepartsListiew.as_view(),
    #     name="exterior",
    # ),
    # path(
    #     "sparepart/category/exterior/tail_lights/",
    #     views.TailLightsListiew.as_view(),
    #     name="tail_lights",
    # ),
    # path(
    #     "sparepart/category/exterior/side_mirrors/",
    #     views.SideMirrorsListiew.as_view(),
    #     name="side_mirrors",
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
    #     "sparepart/category/exterior/led_lights/",
    #     views.LEDLightsListiew.as_view(),
    #     name="led_lights",
    # ),
    # path(
    #     "sparepart/category/exterior/signal_lights/",
    #     views.SignalLightsListiew.as_view(),
    #     name="signal_lights",
    # ),
    # path(
    #     "sparepart/category/exterior/doors/",
    #     views.DoorsListiew.as_view(),
    #     name="doors",
    # ),
    # path(
    #     "sparepart/category/exterior/headlamps/",
    #     views.HeadlampsListiew.as_view(),
    #     name="headlamps",
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
    # path(
    #     "sparepart/category/exterior/fog_lamps/",
    #     views.FogLampsListiew.as_view(),
    #     name="fog_lamps",
    # ),
    # # ==========Interior category & subcategories==========
    # path(
    #     "sparepart/category/interior/",
    #     views.InteriorSparepartsListiew.as_view(),
    #     name="interior",
    # ),
    # path(
    #     "sparepart/category/interior/floor_mats/",
    #     views.FloorMatsListiew.as_view(),
    #     name="floor_mats",
    # ),
    # path(
    #     "sparepart/category/interior/cameras/",
    #     views.CamerasListiew.as_view(),
    #     name="cameras",
    # ),
    # path(
    #     "sparepart/category/interior/seat_covers/",
    #     views.SeatCoversListiew.as_view(),
    #     name="seat_covers",
    # ),
    # path(
    #     "sparepart/category/interior/cooling_systems/",
    #     views.CoolingSystemsListiew.as_view(),
    #     name="cooling_systems",
    # ),
    # path(
    #     "sparepart/category/interior/timing_kits/",
    #     views.TimingKitsListiew.as_view(),
    #     name="timing_kits",
    # ),
    # # ==========Accessories category & subcategories==========
    # path(
    #     "sparepart/category/accessories/",
    #     views.AccessoriesSparepartsListiew.as_view(),
    #     name="accessories",
    # ),
    # # ==========Audio & Videos category & subcategories==========
    # path(
    #     "sparepart/category/audios/",
    #     views.AudioSparepartsListiew.as_view(),
    #     name="audio",
    # ),
    # # ==========Engine category & subcategories==========
    # path(
    #     "sparepart/category/engine/",
    #     views.EngineSparepartsListiew.as_view(),
    #     name="engine",
    # ),
    # # ==========Performance category & subcategories==========
    # path(
    #     "sparepart/category/performance/",
    #     views.PerformanceSparepartsListiew.as_view(),
    #     name="performance",
    # ),
    # # ==========Suspension category & subcategories==========
    # path(
    #     "sparepart/category/suspension/",
    #     views.SuspensionSparepartsListiew.as_view(),
    #     name="suspension",
    # ),
    # # ==========Transmission category & subcategories==========
    # path(
    #     "sparepart/category/transmission/",
    #     views.TransmissionSparepartsListiew.as_view(),
    #     name="transmission",
    # ),
    # # ==========Wheels & Tyres category & subcategories==========
    # path(
    #     "sparepart/category/wheels/",
    #     views.WheelsSparepartsListiew.as_view(),
    #     name="wheels",
    # ),
    # # ==========Electrical category & subcategories==========
    # path(
    #     "sparepart/category/electrical/",
    #     views.ElectricalSparepartsListiew.as_view(),
    #     name="electrical",
    # ),
    # path(
    #     "spareparts/search/",
    #     views.SearchResultsView.as_view(),
    #     name="search_results",
    # ),
]
