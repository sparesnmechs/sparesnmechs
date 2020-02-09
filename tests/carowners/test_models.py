"""Test carowners model."""
import pytest

pytestmark = pytest.mark.django_db


def test_cars_model(car_make, car_model):
    """Test cars."""
    assert car_make.name == "Toyota"
    assert car_model.name == "Harrier"
    assert car_model.car_make.name == "Toyota"


def test_car_owner(car_owner, car_model, car_make):
    """Test car owner."""
    assert car_owner.first_name == "Maich"
    assert car_owner.last_name == "Wetu"
    assert car_owner.phone_number == "0709879098"
    # assert car_owner.car_make == car_make
    # assert car_owner.car_model == car_model
