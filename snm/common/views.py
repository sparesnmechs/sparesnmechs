"""Views."""
from django.urls import reverse
from django.views.generic import CreateView


from .models import Store


class DealerStoreCreateView(CreateView):
    """Generic view to create a store."""

    model = Store
    fields = [
        "name",
        "description",
    ]

    def get_success_url(self):
        """Redirect to creating spareparts."""
        return reverse("sparedealers:create")


class MechStoreCreateView(CreateView):
    """Generic view to create a store."""

    model = Store
    fields = [
        "name",
        "description",
    ]

    def get_success_url(self):
        """Redirect to creating speciality."""
        return reverse("mechanics:create")
