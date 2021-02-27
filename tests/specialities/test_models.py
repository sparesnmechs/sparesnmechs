"""Spareparts model test file."""
import pytest
import snm.specialities.models as models

pytestmark = pytest.mark.django_db


def test_create_a_car_make(car_make):
    """Test creating a car make."""
    car_makes = models.CarMake.objects.all()

    assert car_make
    assert car_make.name == "Volkswagen"
    assert len(car_makes) == 1


def test_car_make_str_representation(car_make):
    """Test car make string representation."""
    assert str(car_make) == "Volkswagen"


def test_create_a_car_model(car_model):
    """Test creating a spare part sub-category."""
    car_models = models.CarMake.objects.all()

    assert car_model
    assert car_model.name == "Golf"
    assert car_model.car_make.name == "Volkswagen"
    assert len(car_models) == 1


def test_car_model_str_representation(car_model):
    """Test car model string representation."""
    assert str(car_model) == "Golf"


def test_create_a_speciality(speciality):
    """Test creating a peciality."""
    specialities = models.Speciality.objects.all()

    assert speciality
    assert len(specialities) == 1


def test_speciality_str_representation(speciality):
    """Test specialities string representation."""
    assert str(speciality) == "Electrical"
