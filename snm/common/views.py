"""Common views."""
from django.views.generic import TemplateView


class WelcomePage(TemplateView):
    """Common home view."""

    template_name = "welcome_page.html"
