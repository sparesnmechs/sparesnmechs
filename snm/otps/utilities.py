"""Otps app utilities."""
import math
import random

from snm.otps.models import Otp


def generateOTP():
    """Generate 6 random numeric OTP."""
    numbers = "0123456789"
    otp = ""
    for i in range(6):
        otp += numbers[math.floor(random.random() * 10)]

    return otp


def verifyOTP(otp):
    """Verify a sent OTP."""
    code = Otp.objects.get(code=otp, is_verified=False)
    if code is None:
        return Exception(f"{otp} is not a valid verification code")

    code.is_verified = True
    code.save()

    return otp
