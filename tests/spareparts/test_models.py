"""Test spareparts model."""
import pytest

pytestmark = pytest.mark.django_db


def test_spareparts_models(
    spare_part,
    spare_part_category,
    spare_part_subcategory,
    speciality,
    car_make,
    car_model,
):
    """Test the various fields in the model."""
    # Spare part
    assert spare_part.name == "bumper"
    assert spare_part.year_of_manufacture == "2019"
    assert spare_part.category.name == spare_part_category.name
    assert spare_part.sub_category.name == spare_part_subcategory.name
    assert spare_part.car_make.name == car_make.name
    assert spare_part.car_model.name == car_model.name

    # Speciality
    assert speciality.name == "service"
    assert speciality.car_make == car_make

    # Cars
    assert car_make.name == "Toyota"
    assert car_model.name == "Harrier"
    assert car_model.car_make.name == "Toyota"


def test_common(common):
    """Test the common fileds."""
    assert common.first_name == "Fundi"
    assert common.last_name == "Wa Magari"
    assert common.phone_number == "+254711223344"
    assert common.description == "Nimeivisha kupaka rangi"


def test_store(store):
    """Test if store is created."""
    assert store.name == "duka"
    assert store.description == "duka ya magari noma"


def test_spare_dealer(store, spare_dealer, spare_part):
    """Test spare dealer."""
    assert spare_dealer.spare_parts == spare_part
    assert spare_dealer.first_name == "Fundi"
    assert spare_dealer.last_name == "Wa Magari"
    assert spare_dealer.phone_number == "+254711223344"
    assert spare_dealer.store.name == store.name
    assert spare_dealer.description == "Nimeivisha kupaka rangi"


def test_mechanic(store, mechanic, speciality):
    """Test mechanic."""
    assert mechanic.speciality == speciality
    assert mechanic.first_name == "Njoro"
    assert mechanic.last_name == "Njoro"
    assert mechanic.phone_number == "+254712345678"
    assert mechanic.store.name == store.name
    assert mechanic.description == "Njoro wa Uber"


def test_car_owner(car_owner, car_model, car_make):
    """Test car owner."""
    assert car_owner.first_name == "Maich"
    assert car_owner.last_name == "Wetu"
    assert car_owner.phone_number == "+254709879098"
    assert car_owner.car_make == car_make
    assert car_owner.car_model == car_model