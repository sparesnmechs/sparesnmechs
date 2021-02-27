"""Spareparts model test file."""
import pytest
import snm.userprofiles.models as models

pytestmark = pytest.mark.django_db


def test_create_a_user_profile(user_profile):
    """Test creating a user profile."""
    user_profiles = models.UserProfile.objects.all()

    assert user_profile
    assert len(user_profiles) == 1


def test_user_profile_str_representation(user_profile):
    """Test car make string representation."""
    assert str(user_profile) == "John Doe"
