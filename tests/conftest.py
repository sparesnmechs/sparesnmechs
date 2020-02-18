"""Common fixture functions."""
import pytest
from model_bakery import baker

from snm.carowners.models import CarMake, CarModel, CarOwner
from snm.common.models import Store
from snm.mechanics.models import Mechanic, Speciality
from snm.sparedealers.models import (
    SpareDealer,
    SparePart,
    SparePartCategory,
    SparePartSubCategory,
)

pytestmark = pytest.mark.django_db


@pytest.fixture
def car_make():
    """Car make."""
    return baker.make(CarMake, name="Toyota", description="Gari ya nguvu")


@pytest.fixture
def car_model(car_make):
    """Car model."""
    return baker.make(CarModel, name="Harrier", car_make=car_make)


@pytest.fixture
def spare_part_category():
    """Spare part category."""
    return baker.make(
        SparePartCategory, name="Ya Nje", description="Parts za nje",
    )


@pytest.fixture
def spare_part_subcategory(spare_part_category):
    """Spare part sub category."""
    return baker.make(
        SparePartSubCategory,
        name="Iko kwa ya nje",
        description="Iko kwa Parts za nje",
    )


@pytest.fixture
def spare_part(
    spare_part_category,
    spare_part_subcategory,
    car_make,
    car_model,
    spare_dealer,
):
    """Spare part."""
    return baker.make(
        SparePart,
        name="bumper",
        description="All new bumper",
        price="10000",
        condition="new",
        year_of_manufacture="2019",
        category=spare_part_category,
        sub_category=spare_part_subcategory,
        car_make=car_make,
        car_model=car_model,
        sparedealer=spare_dealer,
    )


@pytest.fixture
def speciality(car_make):
    """Speciality category."""
    return baker.make(
        Speciality,
        name="service",
        description="General servicing",
        car_make=car_make,
    )


@pytest.fixture
def store():
    """Store."""
    return baker.make(Store, name="duka", description="duka ya magari noma",)


# @pytest.fixture
# def common_user():
#     """Common."""
#     return baker.make(
#         CommonUserFields,
#         first_name="Fundi",
#         last_name="Wa Magari",
#         phone_number="0711223344",
#         description="Nimeivisha kupaka rangi",
#     )


# @pytest.fixture
# def common_item():
#     """Common."""
#     return baker.make(
#         CommonItemFields, name="Item", description="Nimeivisha kupaka rangi",
#     )


@pytest.fixture
def spare_dealer(store):
    """Spare dealer."""
    return baker.make(
        SpareDealer,
        first_name="Fundi",
        last_name="Wa Magari",
        phone_number="0711223344",
        description="Nimeivisha kupaka rangi",
        store=store,
    )


@pytest.fixture
def mechanic(store, speciality):
    """Mechanic."""
    return baker.make(
        Mechanic,
        first_name="Njoro",
        last_name="Njoro",
        phone_number="0712345678",
        description="Njoro wa Uber",
        store=store,
        speciality=speciality,
    )


@pytest.fixture
def car_owner(car_model, car_make):
    """Car owner."""
    return baker.make(
        CarOwner,
        first_name="Maich",
        last_name="Wetu",
        phone_number="0709879098",
        # car_make=car_make,
        # car_model=car_model,
    )
