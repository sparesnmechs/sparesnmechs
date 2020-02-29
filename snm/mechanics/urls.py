"""Mechanics app urls."""
from django.urls import path

from . import views

app_name = "mechanics"
urlpatterns = [
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
    path(
        "mechanic/create",
        views.MechanicCreateView.as_view(),
        name="mech_create",
    ),
    path(
        "mechanic/update/<int:pk>/",
        views.MechanicUpdateView.as_view(),
        name="mech_update",
    ),
    path("mechanic/", views.MechanicListView.as_view(), name="mechanic",),
    path(
        "mechanic/<int:pk>",
        views.MechanicDetailView.as_view(),
        name="mechanic_detail",
    ),
    path('search/', views.SearchResultsView.as_view(), name='search_results'),
]
