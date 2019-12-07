"""Client urls."""
from django.conf.urls import url

from . import views

app_name = "clients"
urlpatterns = [
    url(regex=r"^$", view=views.SpareDealerListView.as_view(), name="list"),
    url(
        regex=r"^(?P<pk>\d+)/$",
        view=views.SpareDealerDetailView.as_view(),
        name="detail",
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.SpareDealerResultsView.as_view(),
        name="results",
    ),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.SpareDealerUpdateView.as_view(),
        name="update",
    ),
    url(regex=r"^$", view=views.MechanicListView.as_view(), name="list"),
    url(
        regex=r"^(?P<pk>\d+)/$", view=views.MechanicDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.MechanicResultsView.as_view(),
        name="results",
    ),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.MechanicUpdateView.as_view(),
        name="update",
    ),
    url(
        regex=r"^(?P<pk>\d+)/$", view=views.CarOwnerDetailView.as_view(),
        name="detail"
    ),
    url(
        regex=r"^(?P<pk>\d+)/results/$",
        view=views.CarOwnerResultsView.as_view(),
        name="results",
    ),
    url(
        regex=r"^(?P<pk>\d+)/update/$",
        view=views.CarOwnerUpdateView.as_view(),
        name="update",
    ),
]
