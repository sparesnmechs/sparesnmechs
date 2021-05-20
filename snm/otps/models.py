"""OTPs app models."""
from django.db import models
from phonenumber_field.validators import validate_international_phonenumber


class Otp(models.Model):
    """OTP data model."""

    phone_number = models.CharField(
        max_length=15,
        validators=[validate_international_phonenumber],
        blank=True,
        null=True,
    )
    email = models.EmailField(blank=True, null=True)
    code = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False)
