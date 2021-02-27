"""Spareparts model test file."""
import pytest
import snm.spareparts.models as models

pytestmark = pytest.mark.django_db


def test_create_a_spare_part_category(category):
    """Test creating a spare part category."""
    categories = models.SparePartCategory.objects.all()

    assert category
    assert category.name == "Exterior"
    assert len(categories) == 1


def test_category_str_representation(category):
    """Test spare part category string representation."""
    assert str(category) == "Exterior"


def test_create_a_spare_part_sub_category(sub_category):
    """Test creating a spare part sub-category."""
    sub_categories = models.SparePartSubCategory.objects.all()

    assert sub_category
    assert sub_category.name == "Doors"
    assert sub_category.category.name == "Exterior"
    assert len(sub_categories) == 1


def test_sub_category_str_representation(sub_category):
    """Test spare part sub-category string representation."""
    assert str(sub_category) == "Doors"


def test_create_a_spare_part(sparepart):
    """Test creating a sparepart."""
    spareparts = models.SparePart.objects.all()

    assert sparepart
    assert len(spareparts) == 1


def test_spare_part_str_representation(sparepart):
    """Test spare part string representation."""
    assert str(sparepart) == "Mark X left rear door"
