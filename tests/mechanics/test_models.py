"""Test mechanics model."""
import pytest

pytestmark = pytest.mark.django_db


def test_mechanics_models(
    speciality, car_make,
):
    """Test the various fields in the model."""
    assert speciality.name == "service"
    assert speciality.car_make == car_make


def test_mechanic(store, mechanic, speciality):
    """Test mechanic."""
    assert mechanic.speciality == speciality
    assert mechanic.first_name == "Njoro"
    assert mechanic.last_name == "Njoro"
    assert mechanic.phone_number == "0712345678"
    assert mechanic.store.name == store.name
    assert mechanic.description == "Njoro wa Uber"
