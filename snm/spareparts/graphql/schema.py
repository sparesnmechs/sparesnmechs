"""GraphQL schema file."""
import graphene
from graphene_django.filter import DjangoFilterConnectionField

from snm.spareparts.graphql.inputs import SparePartInput
from snm.spareparts.graphql.types import (
    CategoryType,
    SparePartNode,
    SparePartType,
    SubCategoryType,
)
from snm.spareparts.models import (
    SparePart,
    SparePartCategory,
    SparePartSubCategory,
)


class Query(graphene.ObjectType):
    """GraphQL query operation type."""

    categories = graphene.List(CategoryType)
    sub_categories = graphene.List(SubCategoryType)
    sub_categories_by_category = graphene.List(
        SubCategoryType, category_id=graphene.String()
    )

    spareparts = graphene.relay.Node.Field(SparePartNode)
    all_spareparts = DjangoFilterConnectionField(SparePartNode)
    spareparts_by_user_id = graphene.List(SparePartType)
    spareparts_by_category = graphene.List(
        SparePartType, category_id=graphene.String()
    )
    spareparts_by_sub_category = graphene.List(
        SparePartType, sub_category_id=graphene.String()
    )

    def resolve_categories(root, info):
        """Categories GraphQL resolver."""
        if not info.context.user.is_authenticated:
            return Exception("Log in first to view categories")

        return SparePartCategory.objects.all()

    def resolve_sub_categories(root, info):
        """Sub Categories GraphQL resolver."""
        if not info.context.user.is_authenticated:
            return Exception("Log in first to view sub-categories")

        return SparePartSubCategory.objects.all()

    def resolve_sub_categories_by_category(root, info, category_id):
        """Get subcategories by category resolver."""
        if not info.context.user.is_authenticated:
            return Exception("Log in first to view sub-categories")

        return SparePartSubCategory.objects.filter(category__id=category_id)

    def resolve_spareparts_by_user_id(root, info):
        """Get sparepart(s) of a given user."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to view your spareparts")

        return SparePart.objects.filter(user_profile__id=user.pk)

    def spareparts_by_category(root, info, category_id):
        """Get spareparts by their subcategories."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to view spareparts by category")

        return SparePart.objects.filter(category__id=category_id)

    def spareparts_by_sub_category(root, info, sub_category_id):
        """Get spareparts by their subcategories."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to view spareparts by subcategory")

        return SparePart.objects.filter(sub_category__id=sub_category_id)


class AddSparePartMutation(graphene.Mutation):
    """Add spareparts GraphQL mutation."""

    class Arguments:
        """The input arguments for this mutation."""

        input = SparePartInput(required=True)

    sparepart = graphene.Field(SparePartType)

    @classmethod
    def mutate(cls, root, info, input=None):
        """Perform the actual add/edit."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to add a sparepart")

        sparepart = SparePart.objects.create(
            created_by=user.pk,
            updated_by=user.pk,
            user_profile=user,
            name=input.name,
            description=input.description,
            condition=input.condition,
            price=input.price,
            category_id=input.category_id,
            sub_category_id=input.sub_category_id,
        )
        sparepart.save()
        return AddSparePartMutation(sparepart=sparepart)


class UpdateSparePartMutation(graphene.Mutation):
    """Add spareparts GraphQL mutation."""

    class Arguments:
        """The input arguments for this mutation."""

        input = SparePartInput()
        sparepart_id = graphene.String()

    sparepart = graphene.Field(SparePartType)

    @classmethod
    def mutate(cls, root, info, sparepart_id, input=None):
        """Perform the actual add/edit."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to update a sparepart")

        sparepart = SparePart.objects.get(pk=sparepart_id)
        if input.name is not None:
            sparepart.name = input.name

        if input.description is not None:
            sparepart.description = input.description

        if input.condition is not None:
            sparepart.condition = input.condition

        if input.price is not None:
            sparepart.price = input.price

        if input.category_id is not None:
            category = SparePartCategory.objects.get(pk=input.category_id)
            sparepart.category = category

        if input.sub_category_id is not None:
            sub_category = SparePartSubCategory.objects.get(
                pk=input.sub_category_id
            )
            sparepart.sub_category = sub_category

        sparepart.save()
        return UpdateSparePartMutation(sparepart=sparepart)


class DeleteSparePartMutation(graphene.Mutation):
    """Mutation to `delete` a spare part."""

    class Arguments:
        """Delete sparepart id."""

        sparepart_id = graphene.String(required=True)

    response = graphene.String()

    @classmethod
    def mutate(cls, root, info, sparepart_id):
        """Perform the actual delete."""
        user = info.context.user
        if not user.is_authenticated:
            return Exception("Log in first to delete a sparepart")

        sparepart = SparePart.objects.get(pk=sparepart_id)
        if sparepart.user_profile.pk != user.pk:
            return Exception("You are not authorized to delete this sparepart")

        sparepart.delete()
        return DeleteSparePartMutation(
            response=f"sparepart with id #{sparepart_id} successfully deleted"
        )


class Mutation(graphene.ObjectType):
    """GraphQL Mutation operation type."""

    add_sparepart = AddSparePartMutation.Field()
    update_sparepart = UpdateSparePartMutation.Field()
    delete_sparepart = DeleteSparePartMutation.Field()
