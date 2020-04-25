"""Sparedealers form."""
from django import forms
from snm.sparedealers.send_email import send_simple_message
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User


class EmailForm(forms.Form):
    """A form to send email."""

    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def save(self):
        """Save user email directly."""
        obj = super(EmailForm, self).save(commit=False)
        obj.email = self.request.user.email
        obj.save()

    def send_email(self):
        """Send an email."""
        message = self.cleaned_data["message"]
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
