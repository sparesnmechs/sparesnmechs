"""Spareparts app urls."""
from django.urls import path

from . import views

app_name = "spareparts"
urlpatterns = [
    path(
        "sparepart",
        views.SparePartListView.as_view(),
        name="sparepart-list",
    ),
    path(
        "sparepart/create",
        views.SparePartCreateView.as_view(),
        name="create",
        ),
    path(
        "sparepart/<int:pk>/",
        views.SparePartUpdateView.as_view(),
        name="update",
        ),
    path(
        "sparepart/<int:pk>/delete",
        views.SparePartDeleteView.as_view(),
        name="delete",
    ),
    path(
        "category",
        views.SparePartListView.as_view(),
        name="category-list",
    ),

    # Speciality
    path(
        "speciality/",
        views.SpecialityListView.as_view(),
        name="speciality-list",
    ),
    path(
        "speciality/create",
        views.SpecialityCreateView.as_view(),
        name="create",
        ),
    path("speciality/<int:pk>/",
    views.SpecialityUpdateView.as_view(),
    name="update",
    ),
    path(
        "speciality/<int:pk>/delete",
        views.SpecialityDeleteView.as_view(),
        name="delete",
    ),
]
