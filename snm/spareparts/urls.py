"""Spareparts app urls."""
from django.conf.urls import url

from . import views

app_name = "spareparts"
urlpatterns = [
    # Sparepart
    url(regex=r"^$", view=views.SparePartCreateView.as_view(), name="create"),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.SparePartUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$", view=views.SparePartDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.SparePartResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.SparePartListView.as_view(), name="list"),
    # Sparepart category
    url(regex=r"^$", view=views.SparePartCategoryCreateView.as_view(),
        name="create"),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.SparePartCategoryUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.SparePartCategoryDetailView.as_view(),
        name="detail",
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.SparePartCategoryResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.SparePartCategoryListView.as_view(),
        name="list"),
    # Sparepart sub-category
    url(
        regex=r"^$", view=views.SparePartSubCategoryCreateView.as_view(),
        name="create"
    ),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.SparePartSubCategoryUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.SparePartSubCategoryDetailView.as_view(),
        name="detail",
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.SparePartSubCategoryResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.SparePartSubCategoryListView.as_view(),
        name="list"),
    # Speciality
    url(regex=r"^$", view=views.SpecialityCreateView.as_view(), name="create"),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.SpecialityUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.SpecialityDetailView.as_view(),
        name="detail",
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.SpecialityResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.SpecialityListView.as_view(), name="list"),
    # Car make
    url(regex=r"^$", view=views.CarMakeCreateView.as_view(), name="create"),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.CarMakeUpdateView.as_view(),
        name="update",
    ),
    url(regex=r"^(?P<pk>\d+)/$",
        view=views.CarMakeDetailView.as_view(), name="detail"),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.CarMakeResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.CarMakeListView.as_view(), name="list"),
    # Car model
    url(regex=r"^$", view=views.CarModelCreateView.as_view(), name="create"),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.CarModelUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$", view=views.CarModelDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.CarModelResultView.as_view(),
        name="results",
    ),
    url(regex=r"^$", view=views.CarModelListView.as_view(), name="list"),
]
