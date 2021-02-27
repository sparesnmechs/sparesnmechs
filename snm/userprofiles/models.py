"""UserProfiles app models."""
from django.contrib.auth.base_user import AbstractBaseUser
from django.core.validators import MaxLengthValidator, RegexValidator
from django.db import models
from django.utils import timezone

from .managers import UserProfileManager


class UserProfile(AbstractBaseUser):
    """UserProfile defines a sparesnmechs user information."""

    phone_number = models.CharField(
        max_length=12,
        unique=True,
        validators=[
            RegexValidator(
                regex="^07[0-9]|^254[0-9]",
                message=(
                    "A valid phone number should "
                    "either start with 07.. or 254.."
                ),
            ),
            MaxLengthValidator(
                limit_value=12, message="An invalid phone number provided"
            ),
        ],
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    objects = UserProfileManager()

    def __str__(self):
        """Represent the UserProfile object in a human readable form."""
        return f"{self.first_name} {self.last_name}"

    def has_perm(self, perm, obj=None):
        """Users have specific permissions."""
        return True

    def has_module_perms(self, app_label):
        """Users have permissions to view the app `app_label`."""
        return True

    @property
    def is_staff(self):
        """Return a user who is a member of the staff."""
        return self.is_admin
