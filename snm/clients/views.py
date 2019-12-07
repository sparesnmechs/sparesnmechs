"""Clients views."""
from django.urls import reverse
from django.views.generic import DetailView, ListView, UpdateView

from .models import CarOwner, Mechanic, SpareDealer


class SpareDealerListView(ListView):
    """Standard spare dealer list view."""
    model = SpareDealer


class SpareDealerDetailView(DetailView):
    """Standard spare dealer detail view."""
    model = SpareDealer


class SpareDealerResultsView(SpareDealerDetailView):
    """Get the results."""
    template_name = 'clients/sparedealer.html'


class SpareDealerUpdateView(UpdateView):
    """Update view for spare dealers."""
    model = SpareDealer

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse('spare_dealer:detail',
                       kwargs={'pk': self.object.pk})


class MechanicListView(ListView):
    """Standard mechanic detail view."""
    model = Mechanic


class MechanicDetailView(DetailView):
    """Standard mechanic detail view."""
    model = Mechanic


class MechanicResultsView(MechanicDetailView):
    """Get mechanic results."""
    template_name = 'clients/mechanic.html'


class MechanicUpdateView(UpdateView):
    """Update view for spare dealers."""
    model = Mechanic

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse('mechanic:detail',
                       kwargs={'pk': self.object.pk})


class CarOwnerDetailView(DetailView):
    """Standard car owner detail view."""
    model = CarOwner


class CarOwnerResultsView(CarOwnerDetailView):
    """Get mechanic results."""
    template_name = 'clients/car_owner.html'


class CarOwnerUpdateView(UpdateView):
    """Update view for spare dealers."""
    model = Mechanic

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse('car_owner:detail',
                       kwargs={'pk': self.object.pk})
