"""GraphQL schema file."""
import graphene
from graphene_django import DjangoObjectType

import snm.spareparts.models as spareparts_models


class CategoryType(DjangoObjectType):
    """CategoryType define a GraphQL spareparts category Object Type."""

    class Meta:
        """Define Meta options."""

        model = spareparts_models.SparePartCategory


class SubCategoryType(DjangoObjectType):
    """SubCategoryType define a GraphQL spareparts sub-category Object Type."""

    class Meta:
        """Define Meta options."""

        model = spareparts_models.SparePartSubCategory


class SparePartType(DjangoObjectType):
    """SparePartType define a GraphQL spareparts Object Type."""

    class Meta:
        """Define Meta options."""

        model = spareparts_models.SparePart


class CategoryInput(graphene.InputObjectType):
    """Sparepart category input."""

    name = graphene.String()


class SubCategoryInput(graphene.InputObjectType):
    """Sparepart sub-category input."""

    name = graphene.String()
    category_id = graphene.String()


class SubCategoryMutation(graphene.Mutation):
    """Add sparepart sub-categories."""

    class Arguments:
        """The input arguments for this mutation."""

        input = SubCategoryInput(required=True)

    sub_category = graphene.Field(SubCategoryType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Perform the actual add/edit."""
        sub_category = spareparts_models.SparePartSubCategory.objects.create(
            name=input.name,
            category_id=input.category_id,
        )
        sub_category.save()
        return SubCategoryMutation(sub_category=sub_category)


class SparePartInput(graphene.InputObjectType):
    """SparePart inputs."""

    name = graphene.String()
    description = graphene.String()
    condition = graphene.String()
    price = graphene.Decimal()
    category_id = graphene.String()
    sub_category_id = graphene.String()


class SparePartMutation(graphene.Mutation):
    """Add spareparts GraphQL mutation."""

    class Arguments:
        """The input arguments for this mutation."""

        input = SparePartInput(required=True)

    sparepart = graphene.Field(SparePartType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Perform the actual add/edit."""
        user = info.context.user
        sparepart = spareparts_models.SparePart.objects.create(
            user_profile=user,
            name=input.name,
            description=input.description,
            condition=input.condition,
            price=input.price,
            category_id=input.category_id,
            sub_category_id=input.sub_category_id,
        )
        sparepart.save()
        return SparePartMutation(sparepart=sparepart)


class Query(graphene.ObjectType):
    """GraphQL query operation type."""

    categories = graphene.List(CategoryType)
    sub_categories = graphene.List(SubCategoryType)

    def resolve_categories(root, info):
        """Categories GraphQL resolver."""
        return spareparts_models.SparePartCategory.objects.all()

    def resolve_sub_categories(root, info):
        """Sub Categories GraphQL resolver."""
        return spareparts_models.SparePartSubCategory.objects.all()


class Mutation(graphene.ObjectType):
    """GraphQL Mutation operation type."""

    add_sparepart = SparePartMutation.Field()
    add_sub_category = SubCategoryMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
