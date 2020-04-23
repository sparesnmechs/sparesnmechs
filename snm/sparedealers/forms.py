"""Send email form."""
from django import forms
from snm.sparedealers.send_email import send_simple_message


class EmailForm(forms.Form):
    """A form to send email."""

    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        """Send an email."""
        message = self.cleaned_data["message"]
        email = self.cleaned_data["email"]

        send_simple_message(message, email)
