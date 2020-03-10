"""Carowners app urls."""
from django.urls import path

from . import views

app_name = "carowners"
urlpatterns = [
    path(
        "carowner/create", views.CarownerCreateView.as_view(), name="create",
    ),
    path(
        "carowner/update/<int:pk>/",
        views.CarownerUpdateView.as_view(),
        name="update",
    ),
    path(
        "carowner/<int:pk>", views.OwnerDetailView.as_view(), name="carowner",
    ),
    path("cars/car_models", views.get_carmodels, name="get_carmodels",),
]
