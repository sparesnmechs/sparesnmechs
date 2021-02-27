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
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self,
        phone_number,
        first_name,
        last_name,
        password=None,
    ):
        """
        Create and save a Super User.

        Creates with the given phone number, names and password.
        """
        user = self.create_user(phone_number, first_name, last_name, password)
        user.is_admin = True
        user.save(using=self._db)

        return user
