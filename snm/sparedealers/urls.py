"""Sparedealers app urls."""
from django.urls import path

from . import views

app_name = "sparedealers"
urlpatterns = [
    path("", views.SparePartListView.as_view(), name="sparepart-list",),
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
        "sparepart/category/exterior/",
        views.ExteriorSparepartsListiew.as_view(),
        name="exterior",
    ),
    path(
        "sparepart/category/interior/",
        views.InteriorSparepartsListiew.as_view(),
        name="interior",
    ),
    path(
        "sparepart/category/accessories/",
        views.AccessoriesSparepartsListiew.as_view(),
        name="accessories",
    ),
    path(
        "sparepart/category/audios/",
        views.AudioSparepartsListiew.as_view(),
        name="audio",
    ),
    path(
        "sparepart/category/engine/",
        views.EngineSparepartsListiew.as_view(),
        name="engine",
    ),
    path(
        "sparepart/category/performance/",
        views.PerformanceSparepartsListiew.as_view(),
        name="performance",
    ),
    path(
        "sparepart/category/suspension/",
        views.SuspensionSparepartsListiew.as_view(),
        name="suspension",
    ),
    path(
        "sparepart/category/transmission/",
        views.TransmissionSparepartsListiew.as_view(),
        name="transmission",
    ),
    path(
        "sparepart/category/wheels/",
        views.WheelsSparepartsListiew.as_view(),
        name="wheels",
    ),
    path(
        "sparepart/category/electrical/",
        views.ElectricalSparepartsListiew.as_view(),
        name="electrical",
    ),
    path("spareparts/search/", views.SearchResultsView.as_view(), name="search_results")
]
