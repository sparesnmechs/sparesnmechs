"""Mechanic form."""
from django import forms
from .models import Mechanic


class MechanicForm(forms.ModelForm):
    """Customize sparepart posting form."""

    class Meta:
        """Meta class."""

        model = Mechanic
        fields = [
            "speciality",
            "car_make",
            "phone_number",
            "location",
            "garage",
            "logo",
        ]
        labels = {
            # "speciality": "",
            # "car_make": "",
            "phone_number": "",
            "location": "",
            "garage": "",
            "logo": "",
        }
        widgets = {
            "speciality": forms.CheckboxSelectMultiple(),
            "car_make": forms.CheckboxSelectMultiple(),
            "phone_number": forms.TextInput(
                attrs={"placeholder": "Phone Number"}
            ),
            "location": forms.TextInput(attrs={"placeholder": "Location"}),
            "garage": forms.TextInput(attrs={"placeholder": "Garage"}),
        }

    # def __init__(self, *args, **kwargs):
    #     super(SellPartForm, self).__init__(*args, **kwargs)
    #     self.fields["category"].empty_label = "Category"
    #     self.fields["sub_category"].empty_label = "Sub Category"
    #     self.fields["car_make"].empty_label = "Car Make"
    #     self.fields["car_model"].empty_label = "Car Model"
