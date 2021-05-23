"""Common urls."""
from django.urls import path

from . import views

app_name = "common"
urlpatterns = [
    path(
        "",
        views.WelcomePage.as_view(),
        name="welcome-page",
    ),
]
