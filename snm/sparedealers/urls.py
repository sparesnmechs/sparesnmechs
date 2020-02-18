"""Sparedealers app urls."""
from django.urls import path

from . import views

app_name = "sparedealers"
urlpatterns = [
    path(
        "",
        views.sparepart_view,
        name="sparepart-list",
    ),
    path(
        "sparepart/create",
        views.SparePartCreateView.as_view(),
        name="create",
        ),
    # path(
    #     "sparepart/<int:pk>/",
    #     views.SparePartUpdateView.as_view(),
    #     name="update",
    #     ),
    # path(
    #     "sparepart/<int:pk>/delete",
    #     views.SparePartDeleteView.as_view(),
    #     name="delete",
    # ),
    # path(
    #     "category/",
    #     views.SparePartListView.as_view(),
    #     name="category-list",
    # ),
]
