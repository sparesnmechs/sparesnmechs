"""Common fixture functions."""
import pytest
import spareparts.models as models
from model_bakery import baker

pytestmark = pytest.mark.django_db


@pytest.fixture
def car_make():
    """Car make."""
    return baker.make(
        models.CarMake,
        name='Toyota',
        description='Gari ya nguvu',
    )


@pytest.fixture
def car_model(car_make):
    """Car model."""
    return baker.make(
        models.CarModel,
        name='Harrier',
        car_make=car_make,
    )


@pytest.fixture
def spare_part_category():
    """Spare part category."""
    return baker.make(
        models.SparePartCategory,
        name='Ya Nje',
        description='Parts za nje',
    )


@pytest.fixture
def spare_part_subcategory(spare_part_category):
    """Spare part sub category."""
    return baker.make(
        models.SparePartSubCategory,
        name='Iko kwa ya nje',
        description='Iko kwa Parts za nje',
    )


@pytest.fixture
def spare_part(spare_part_category, spare_part_subcategory,
               car_make, car_model):
    """Spare part."""
    return baker.make(
        models.SparePart,
        name='bumper',
        description='All new bumper',
        price=10000,
        condition='new',
        year_of_manufacture=2019,
        category=spare_part_category,
        sub_category=spare_part_subcategory,
        car_make=car_make,
        car_model=car_model,
    )


@pytest.fixture
def speciality(car_make):
    """Speciality category."""
    return baker.make(
        models.Speciality,
        name='service',
        description='General servicing',
        car_make=car_make,
    )
