"""Views."""
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .filters import SparePartFilter
from .models import (
    SpareDealer,
    SparePart,
    SparePartCategory,
    SparePartSubCategory,
)


class SparePartCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Create view for spare parts."""

    model = SparePart
    fields = [
        "name",
        "description",
        "price",
        "condition",
        "year_of_manufacture",
        "category",
        "sub_category",
        "car_make",
        "car_model",
        "sparedealer",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully created"


class SparePartUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view for spare parts."""

    model = SparePart
    fields = [
        "name",
        "description",
        "price",
        "condition",
        "year_of_manufacture",
        "category",
        "sub_category",
        "car_make",
        "car_model",
        "sparedealer",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your sparepart has been succesfully updated"


class SparePartDeleteView(LoginRequiredMixin, DeleteView):
    """Delete a sparepart."""

    model = SparePart
    login_url = "login"
    redirect_field_name = "redirect_to"


class SparePartListView(ListView):
    """List view of spareparts."""

    queryset = SparePart.objects.all()
    context_object_name = "spareparts"


class SparePartCategoryListView(ListView):
    """List view of spareparts."""

    queryset = SparePartCategory.objects.all()
    context_object_name = "categories"


class DealerCreateView(SuccessMessageMixin, LoginRequiredMixin, CreateView):
    """Create view for mechanics."""

    model = SpareDealer
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "store",
        "description",
        "photo",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your profile has been succesfully created"

    def get_success_url(self):
        return reverse_lazy(
            "sparedealers:dealer", kwargs={"pk": self.object.pk}
        )


class DealerUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    """Update view for mechanics."""

    model = SpareDealer
    fields = [
        "first_name",
        "last_name",
        "phone_number",
        "store",
        "description",
        "photo",
    ]
    login_url = "login"
    redirect_field_name = "redirect_to"
    success_message = "Your profile has been succesfully updated"

    def get_success_url(self):
        return reverse_lazy(
            "sparedealers:dealer", kwargs={"pk": self.object.pk}
        )


class DealerDetailView(DetailView):
    """View a dealers details."""

    model = SpareDealer
    context_object_name = "dealers"


def sparepart_view(request):
    """Search view."""
    spareparts_filter = SparePartFilter(
        request.GET, queryset=SparePart.objects.all()
    )
    return render(
        request,
        "sparedealers/sparepart_list.html",
        {"filter": spareparts_filter},
    )


def get_subcategories(request):
    category = request.GET.get("category", None)
    if not category:
        return HttpResponse(
            serializers.serialize("json", SparePartSubCategory.objects.all()),
            content_type="application/json",
        )
    sub_categories = SparePartSubCategory.objects.filter(category=category)
    return HttpResponse(
        serializers.serialize("json", sub_categories),
        content_type="application/json",
    )
