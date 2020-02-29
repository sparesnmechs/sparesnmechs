"""Dealer creation form."""
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import CustomUser, SpareDealer


class DealerSignUpForm(UserCreationForm):
    """Create the sign up form."""

    class Meta(UserCreationForm.Meta):
        """Meta class."""

        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dealer = True
        user.save()
        SpareDealer.objects.create(user=user)
        return user
