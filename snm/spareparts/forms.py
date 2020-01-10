"""Forms for the spareparts app."""
from django import forms

from .models import (CarMake, CarModel, SparePart, SparePartCategory,
                     SparePartSubCategory, Speciality)


class CarMakeForm(forms.ModelForm):
    """Car make form."""

    class Meta:
        """Use model fields."""

        fields = ["name", "description"]
        model = CarMake


class CarModelForm(forms.ModelForm):
    """Car model form."""

    class Meta:
        """Use model fields."""

        fields = ["name", "description", "car_make"]
        model = CarModel


class SparePartForm(forms.ModelForm):
    """Spareparts form."""

    class Meta:
        """Use model fields."""

        model = SparePart
        fields = [
            'name', 'description', 'price', 'condition',
            'year_of_manufacture', 'category', 'sub_category',
            'car_make', 'car_model', 'photo'
            ]

        # TODO How to handle photo in forms


class SparePartCategoryForm(forms.ModelForm):
    """Spareparts categories form."""

    class Meta:
        """Use model fields."""

        model = SparePartCategory
        fields = ['name', 'description']


class SparePartSubCategoryForm(forms.ModelForm):
    """Spareparts sub-categories form."""

    class Meta:
        """Use model fields."""

        model = SparePartSubCategory
        fields = ['name', 'description', 'category']


class SpecialityForm(forms.ModelForm):
    """Speciality form."""

    class Meta:
        """Use model fields."""

        model = Speciality
        fields = ['name', 'description', 'car_make']
