"""App admin."""
from django.contrib import admin

from snm.otps.models import Otp

admin.site.register(Otp)
