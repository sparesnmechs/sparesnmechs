"""Mechanics app urls."""
from django.urls import path

from . import views

app_name = "mechanics"
urlpatterns = [
    path("mechanic/", views.filtered_mechanic_list, name="mechanic",),
    path(
        "mechanic/create", views.MechanicCreateView.as_view(), name="create",
    ),
    path(
        "mechanic/<int:pk>/",
        views.MechanicUpdateView.as_view(),
        name="update",
    ),
    path(
        "mechanic/<int:pk>/delete",
        views.MechanicDeleteView.as_view(),
        name="delete",
    ),
    path(
        "mechanic/<int:pk>", views.MechanicDetailView.as_view(), name="detail",
    ),
    path("search/", views.SearchResultsView.as_view(), name="search_results"),
    path(
        "mechanic/listings/",
        views.MechanicListingsListView.as_view(),
        name="listings",
    ),
    path(
        "mechanic/category/body_work/",
        views.BodyWorkListView.as_view(),
        name="body_work",
    ),
    path(
        "mechanic/category/electrical/",
        views.ElectricalListView.as_view(),
        name="electrical",
    ),
    path(
        "mechanic/category/mechanical/",
        views.MechanicalListView.as_view(),
        name="mechanical",
    ),
]
