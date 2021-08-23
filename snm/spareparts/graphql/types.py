"""GraphQL types."""
from graphene import relay
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


class SparePartNode(DjangoObjectType):
    """SparePartNode define a GraphQL spareparts Object Type Node."""

    class Meta:
        """Define Meta options."""

        model = SparePart
        filter_fields = {
            "category__id": ["exact"],
            "sub_category__id": ["exact"],
            "condition": ["exact"],
            "price": ["gt", "lt"],
        }
        interfaces = (relay.Node,)
