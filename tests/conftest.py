"""Common fixture functions."""
import pytest
from model_bakery import baker

import snm.spareparts.models as models
from snm.clients.models import CarOwner, Common, Mechanic, SpareDealer, Store

pytestmark = pytest.mark.django_db


@pytest.fixture
def car_make():
    """Car make."""
    return baker.make(models.CarMake, name="Toyota",
                      description="Gari ya nguvu",)


@pytest.fixture
def car_model(car_make):
    """Car model."""
    return baker.make(models.CarModel, name="Harrier", car_make=car_make,)


@pytest.fixture
def spare_part_category():
    """Spare part category."""
    return baker.make(
        models.SparePartCategory, name="Ya Nje", description="Parts za nje",
    )


@pytest.fixture
def spare_part_subcategory(spare_part_category):
    """Spare part sub category."""
    return baker.make(
        models.SparePartSubCategory,
        name="Iko kwa ya nje",
        description="Iko kwa Parts za nje",
    )


@pytest.fixture
def spare_part(spare_part_category, spare_part_subcategory, car_make,
               car_model
               ):
    """Spare part."""
    return baker.make(
        models.SparePart,
        name="bumper",
        description="All new bumper",
        price="10000",
        condition="new",
        year_of_manufacture="2019",
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
        name="service",
        description="General servicing",
        car_make=car_make,
    )


@pytest.fixture
def store():
    """Store."""
    return baker.make(Store, name="duka", description="duka ya magari noma",)


@pytest.fixture
def common():
    """Common."""
    return baker.make(
        Common,
        first_name="Fundi",
        last_name="Wa Magari",
        phone_number="+254711223344",
        description="Nimeivisha kupaka rangi",
    )


@pytest.fixture
def spare_dealer(store, spare_part):
    """Spare dealer."""
    return baker.make(
        SpareDealer,
        first_name="Fundi",
        last_name="Wa Magari",
        phone_number="+254711223344",
        description="Nimeivisha kupaka rangi",
        store=store,
        spare_parts=spare_part,
    )


@pytest.fixture
def mechanic(store, speciality):
    """Mechanic."""
    return baker.make(
        Mechanic,
        first_name="Njoro",
        last_name="Njoro",
        phone_number="+254712345678",
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
        phone_number="+254709879098",
        car_make=car_make,
        car_model=car_model,
    )
