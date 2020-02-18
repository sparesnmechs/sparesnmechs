"""Common app urls."""
from django.urls import path

from . import views

app_name = "common"
urlpatterns = [
    path(
        "dealer_store/create/",
        views.DealerStoreCreateView.as_view(),
        name="dealer_create",
    ),
    path(
        "mech_store/create/",
        views.MechStoreCreateView.as_view(),
        name="mech_create",
    ),
]
