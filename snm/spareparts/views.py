"""Spare parts views."""
from django.contrib import messages
from django.urls import reverse
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import (
    CarMake,
    CarModel,
    SparePart,
    SparePartCategory,
    SparePartSubCategory,
    Speciality,
)


class SparePartMixin:
    """Common spare part view behaviours."""

    fields = ["__all__"]

    @property
    def success_message(self):
        """Success msg."""
        return NotImplemented

    def form_valid(self):
        """Display the success msg when the form is valid."""
        messages.info(self.request, self.success_message)
        return super(SparePartMixin, self).form_valid(form)


class SparePartCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = SparePart
    success_message = "Spare part created!"


class SparePartUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = SparePart
    success_message = "Spare part updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("spare_part:detail", kwargs={"pk": self.object.pk})


class SparePartDetailView(DetailView):
    """Detail view for spare parts."""

    model = SparePart


class SparePartResultView(SparePartDetailView):
    """Render the result."""

    template_name = "spareparts/sparepart.html"


class SparePartListView(ListView):
    """List view for spare parts with search functionality."""

    model = SparePart

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(SparePartListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset


class SparePartCategoryCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = SparePartCategory
    success_message = "Spare part category created!"


class SparePartCategoryUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = SparePartCategory
    success_message = "Spare part category updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("spare_part_category:detail",
                       kwargs={"pk": self.object.pk})


class SparePartCategoryDetailView(DetailView):
    """Detail view for spare parts."""

    model = SparePartCategory


class SparePartCategoryResultView(SparePartCategoryDetailView):
    """Render the result."""

    template_name = "spareparts/spare_part_category.html"


class SparePartCategoryListView(ListView):
    """List view for spare parts with search functionality."""

    model = SparePartCategory

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(SparePartCategoryListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset


class SparePartSubCategoryCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = SparePartSubCategory
    success_message = "Spare part sub-category created!"


class SparePartSubCategoryUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = SparePartSubCategory
    success_message = "Spare part sub-category updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("spare_part_sub_category:detail",
                       kwargs={"pk": self.object.pk})


class SparePartSubCategoryDetailView(DetailView):
    """Detail view for spare parts."""

    model = SparePartSubCategory


class SparePartSubCategoryResultView(SparePartSubCategoryDetailView):
    """Render the result."""

    template_name = "spareparts/spare_part_sub_category.html"


class SparePartSubCategoryListView(ListView):
    """List view for spare parts with search functionality."""

    model = SparePartSubCategory

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(SparePartSubCategoryListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset


class SpecialityCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = Speciality
    success_message = "Speciality created!"


class SpecialityUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = Speciality
    success_message = "Speciality updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("speciality:detail", kwargs={"pk": self.object.pk})


class SpecialityDetailView(DetailView):
    """Detail view for spare parts."""

    model = Speciality


class SpecialityResultView(SpecialityDetailView):
    """Render the result."""

    template_name = "spareparts/speciality.html"


class SpecialityListView(ListView):
    """List view for spare parts with search functionality."""

    model = Speciality

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(SpecialityListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset


class CarMakeCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = CarMake
    success_message = "Car make created!"


class CarMakeUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = CarMake
    success_message = "Car make updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("car_make:detail", kwargs={"pk": self.object.pk})


class CarMakeDetailView(DetailView):
    """Detail view for spare parts."""

    model = CarMake


class CarMakeResultView(CarMakeDetailView):
    """Render the result."""

    template_name = "spareparts/car_make.html"


class CarMakeListView(ListView):
    """List view for spare parts with search functionality."""

    model = CarMake

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(CarMakeListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset


class CarModelCreateView(SparePartMixin, CreateView):
    """Create view for spare parts."""

    model = CarModel
    success_message = "Car model created!"


class CarModelUpdateView(SparePartMixin, UpdateView):
    """Update view for spare parts."""

    model = CarModel
    success_message = "Car model updated!"

    def get_success_url(self):
        """Reverse to detail page after successful update."""
        return reverse("car_model:detail", kwargs={"pk": self.object.pk})


class CarModelDetailView(DetailView):
    """Detail view for spare parts."""

    model = CarModel


class CarModelResultView(CarModelDetailView):
    """Render the result."""

    template_name = "spareparts/car_model.html"


class CarModelListView(ListView):
    """List view for spare parts with search functionality."""

    model = CarModel

    def get_queryset(self):
        """Fetch query set from the parent query_set."""
        queryset = super(CarModelListView, self).get_queryset()

        # Get the q GET parameter
        q = self.request.GET.get("q")  # Naive search. TODO Exploit further
        if q:
            # Return filtered queryset
            return queryset.filter(name__icontain=q)
        # Return base queryset
        return queryset
