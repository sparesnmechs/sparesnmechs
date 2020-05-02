"""Sparedealers form."""
from django import forms
from snm.sparedealers.send_email import send_simple_message
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import SparePart


class EmailForm(forms.Form):
    """A form to send email."""

    email = forms.EmailField(required=False)
    # message = forms.CharField(widget=forms.Textarea)
    car_make = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Car Make - Toyota Vitz"}
        ),
        label="",
    )
    chasis_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Chasis Number"}),
        label="",
    )
    part = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Part(s) you are requesting for"}
        ),
        label="",
    )
    location = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Location"}), label="",
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={"placeholder": "Phone Number"}),
        label="",
    )  # Needs validation

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


class SellPartForm(forms.ModelForm):
    """Customize sparepart posting form."""

    class Meta:
        """Meta class."""

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
            "phone_number",
            "location",
            "store",
            "photo",
        ]
        labels = {
            "name": "",
            "description": "",
            "price": "",
            "condition": "",
            "year_of_manufacture": "",
            "category": "",
            "sub_category": "",
            "car_make": "",
            "car_model": "",
            "phone_number": "",
            "location": "",
            "store": "",
            "photo": "",
        }
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Name"}),
            "description": forms.TextInput(
                attrs={"placeholder": "Description"}
            ),
            "price": forms.TextInput(attrs={"placeholder": "Price"}),
            "condition": forms.Select(attrs={"placeholder": "Condition"}),
            "year_of_manufacture": forms.TextInput(
                attrs={"placeholder": "Year of Manufacture"}
            ),
            "category": forms.Select(attrs={"placeholder": "Category"}),
            "sub_category": forms.Select(
                attrs={"placeholder": "Sub Category"}
            ),
            "car_make": forms.Select(attrs={"placeholder": "Car Make"}),
            "car_model": forms.Select(attrs={"placeholder": "Car Model"}),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "Phone Number"}
            ),
            "location": forms.TextInput(attrs={"placeholder": "Location"}),
            "store": forms.TextInput(attrs={"placeholder": "Store"}),
        }

    def __init__(self, *args, **kwargs):
        super(SellPartForm, self).__init__(*args, **kwargs)
        self.fields["category"].empty_label = "Category"
        self.fields["sub_category"].empty_label = "Sub Category"
        self.fields["car_make"].empty_label = "Car Make"
        self.fields["car_model"].empty_label = "Car Model"
        self.fields["condition"].empty_label = "Condition"
