"""Test common model."""
import pytest

pytestmark = pytest.mark.django_db


def test_common_user_fields(common_user):
    """Test the common fileds."""
    assert common_user.first_name == "Fundi"
    assert common_user.last_name == "Wa Magari"
    assert common_user.phone_number == "0711223344"
    assert common_user.description == "Nimeivisha kupaka rangi"


def test_common_user_fields_str(common_user):
    """Test string representation."""
    assert str(common_user) == 'Fundi Wa Magari'


def test_common_item_fields_str(common_item):
    """Test string representation."""
    assert str(common_item) == 'Item'


def test_common_item_fields(common_item):
    """Test the common fileds."""
    assert common_item.name == "Item"
    assert common_item.description == "Nimeivisha kupaka rangi"


def test_store(store):
    """Test if store is created."""
    assert store.name == "duka"
    assert store.description == "duka ya magari noma"
