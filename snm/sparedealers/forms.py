"""Sparedealers form."""
from django import forms
from snm.sparedealers.send_email import send_simple_message
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class EmailForm(forms.Form):
    """A form to send email."""

    email = forms.EmailField(required=False)
    # message = forms.CharField(widget=forms.Textarea)
    car_make = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Toyota Vits"})
    )
    chasis_number = forms.CharField()
    part = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Part(s) you are requesting for"}
        )
    )
    location = forms.CharField()
    phone_number = forms.CharField()  # Needs validation

    def save(self):
        """Save user email directly."""
        obj = super(EmailForm, self).save(commit=False)
        obj.email = self.request.user.email
        obj.save()

    def send_email(self):
        """Send an email."""
        car_make = self.cleaned_data["car_make"]
        chasis_number = self.cleaned_data["chasis_number"]
        part = self.cleaned_data["part"]
        location = self.cleaned_data["location"]
        phone_number = self.cleaned_data["phone_number"]
        message = (
            f"A request has been made for {car_make} "
            f"{part} with chasis number {chasis_number} "
            f"from {location} by {phone_number}"
        )
        email = self.cleaned_data["email"]

        send_simple_message(message, email)


class CustomUserCreationForm(UserCreationForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email", "first_name", "last_name")
        help_texts = {
            "username": None,
            "email": None,
        }


class CustomUserChangeForm(UserChangeForm):
    """Create a custom user form."""

    class Meta:
        """Models meta class."""

        model = User
        fields = ("username", "email", "first_name", "last_name")
