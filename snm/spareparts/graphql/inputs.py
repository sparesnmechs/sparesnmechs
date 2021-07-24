"""GraphQL inputs file."""
import graphene


class SparePartInput(graphene.InputObjectType):
    """SparePart inputs."""

    name = graphene.String()
    description = graphene.String()
    condition = graphene.String()
    price = graphene.Decimal()
    category_id = graphene.String()
    sub_category_id = graphene.String()
