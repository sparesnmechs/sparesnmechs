"""Mechanic creation form."""
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, Mechanic


class MechanicSignUpForm(UserCreationForm):
    """Create the sign up form."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser

    @transaction.atomic
    def save(self):
        """Save function."""
        user = super().save(commit=False)
        user.is_mechanic = True
        user.save()
        Mechanic.objects.create(user=user)
        return user
