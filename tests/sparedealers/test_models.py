"""Test sparedealers model."""
import pytest

pytestmark = pytest.mark.django_db


def test_spareparts_models(
    spare_part,
    spare_part_category,
    spare_part_subcategory,
    car_make,
    car_model,
    spare_dealer,
):
    """Test the various fields in the model."""
    # Spare part
    assert spare_part.name == "bumper"
    assert spare_part.year_of_manufacture == "2019"
    assert spare_part.category.name == spare_part_category.name
    assert spare_part.sub_category.name == spare_part_subcategory.name
    assert spare_part.car_make.name == car_make.name
    assert spare_part.car_model.name == car_model.name
    assert spare_part.sparedealer == spare_dealer


def test_spare_dealer(spare_dealer):
    """Test spare dealer."""
    assert spare_dealer.first_name == "Fundi"
    assert spare_dealer.last_name == "Wa Magari"
    assert spare_dealer.phone_number == "0711223344"
    assert spare_dealer.store == "store"
    assert spare_dealer.description == "Nimeivisha kupaka rangi"
