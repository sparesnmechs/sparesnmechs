"""UserProfiles app managers."""
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserProfileManager(BaseUserManager):
    """
    A Custom user model manager.

    Where phone number is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(
        self,
        phone_number,
        first_name,
        last_name,
        password=None,
        **extra_fields
    ):
        """
        Create and save a User.

        With the given phone number, names and password.
        """
        if not phone_number:
            raise ValueError(_("Phone number must be set"))
        if not first_name:
            raise ValueError(_("First name must be set"))
        if not last_name:
            raise ValueError(_("Last name must be set"))
        user = self.model(
            phone_number=phone_number,
            first_name=first_name,
            last_name=last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(
        self,
        phone_number,
        first_name,
        last_name,
        password=None,
        **extra_fields
    ):
        """
        Create and save a Super User.

        Creates with the given phone number, names and password.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(
            phone_number, first_name, last_name, **extra_fields
        )
