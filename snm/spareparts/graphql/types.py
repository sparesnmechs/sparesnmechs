"""GraphQL types."""
from graphene_django import DjangoObjectType

from snm.spareparts.models import (
    SparePart,
    SparePartCategory,
    SparePartSubCategory,
)


class CategoryType(DjangoObjectType):
    """CategoryType define a GraphQL spareparts category Object Type."""

    class Meta:
        """Define Meta options."""

        model = SparePartCategory


class SubCategoryType(DjangoObjectType):
    """SubCategoryType define a GraphQL spareparts sub-category Object Type."""

    class Meta:
        """Define Meta options."""

        model = SparePartSubCategory


class SparePartType(DjangoObjectType):
    """SparePartType define a GraphQL spareparts Object Type."""

    class Meta:
        """Define Meta options."""

        model = SparePart
