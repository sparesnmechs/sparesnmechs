"""Car owner creation form."""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CarMake, CarModel, CarOwner, CustomUser


class OwnerSignUpForm(UserCreationForm):
    """Create the sign up form."""

    car_make = forms.ModelChoiceField(queryset=CarMake.objects.all())
    car_model = forms.ModelChoiceField(queryset=CarModel.objects.all())

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_carowner = True
        user.save()
        carowner = CarOwner.objects.create(user=user)
        carowner.car_make = self.cleaned_data.get("car_make")
        carowner.car_model = self.cleaned_data.get("car_model")
        carowner.save()
        return user
