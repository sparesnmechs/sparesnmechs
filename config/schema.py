import graphene

import snm.otps.schema as otp_schema
import snm.spareparts.graphql.schema as spareparts_schema
import snm.userprofiles.schema as user_profile_schema


class Query(
    user_profile_schema.Query,
    otp_schema.Query,
    spareparts_schema.Query,
    graphene.ObjectType,
):
    """GraphQL query type schema."""

    pass


class Mutation(
    user_profile_schema.Mutation,
    otp_schema.Mutation,
    spareparts_schema.Mutation,
    graphene.ObjectType,
):
    """GraphQL mutation type schema."""

    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
