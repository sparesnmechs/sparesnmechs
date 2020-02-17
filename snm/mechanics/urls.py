"""Mechanics app urls."""
from django.urls import path

from . import views

app_name = "mechanics"
urlpatterns = [
    path(
        "speciality/",
        views.speciality_view,
        name="speciality-list",
    ),
    path(
        "speciality/create",
        views.SpecialityCreateView.as_view(),
        name="create",
    ),
    path(
        "speciality/<int:pk>/",
        views.SpecialityUpdateView.as_view(),
        name="update",
    ),
    path(
        "speciality/<int:pk>/delete",
        views.SpecialityDeleteView.as_view(),
        name="delete",
    ),
]
