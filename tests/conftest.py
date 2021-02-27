"""Test fixtures."""

import pytest
from model_bakery import baker

import snm.spareparts.models as models
import snm.specialities.models as specialities_models
import snm.userprofiles.models as user_profile_models

pytestmark = pytest.mark.django_db


@pytest.fixture
def user_profile():
    """Return a user profile."""
    return baker.make(
        user_profile_models.UserProfile,
        phone_number="0700000000",
        first_name="John",
        last_name="Doe",
        email="john.doe@email.com",
    )


@pytest.fixture
def category():
    """Return a sparepart category."""
    return baker.make(
        models.SparePartCategory,
        name="Exterior",
    )


@pytest.fixture
def sub_category(category):
    """Return a sparepart sub-category."""
    return baker.make(
        models.SparePartSubCategory,
        name="Doors",
        category=category,
    )


@pytest.fixture
def sparepart(user_profile, category, sub_category):
    """Return a sparepart."""
    return baker.make(
        models.SparePart,
        user_profile=user_profile,
        name="Mark X left rear door",
        description="Black Mark X left rear door",
        condition="New",
        price="500.00",
        category=category,
        sub_category=sub_category,
    )


@pytest.fixture
def car_make():
    """Return a car make."""
    return baker.make(
        specialities_models.CarMake,
        name="Volkswagen",
    )


@pytest.fixture
def car_model(car_make):
    """Return a car model."""
    return baker.make(
        specialities_models.CarModel,
        name="Golf",
        car_make=car_make,
    )


@pytest.fixture
def speciality(user_profile, car_make, car_model):
    """Return a speciality."""
    return baker.make(
        specialities_models.Speciality,
        user_profile=user_profile,
        name="Electrical",
        description="Repairs VW Golf electrical faults",
        car_make=car_make,
        car_model=car_model,
        price="1.00",
    )
