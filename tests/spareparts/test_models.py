"""Test spareparts model."""
import pytest

pytestmark = pytest.mark.django_db


def test_spareparts_models(
        spare_part, spare_part_category, spare_part_subcategory,
        speciality, car_make, car_model
):
    """Test the various fields in the model."""
    # Spare part
    assert spare_part.name == 'bumper'
    assert spare_part.year_of_manufacture == 2019
    assert spare_part.category.name == spare_part_category.name
    assert (
        spare_part.sub_category.name == spare_part_category.name
    )
    assert spare_part.car_make.name == car_make.name
    assert spare_part.car_model.name == car_model.name

    # Speciality
    assert speciality.name == 'service'
    assert speciality.car_make == car_make

    # Cars
    assert car_make.name == 'Toyota'
    assert car_model.name == 'Harrier'
    assert car_model.car_make.name == 'Toyota'
