"""User profile schema file."""
import graphene
import graphql_jwt
from django.contrib.auth.hashers import check_password
from graphene_django import DjangoObjectType

from snm.userprofiles.models import UserProfile


class UserProfileType(DjangoObjectType):
    """User profile model object type."""

    class Meta:
        """Meta options."""

        model = UserProfile
        fields = (
            "first_name",
            "last_name",
            "phone_number",
            "email",
            "is_active",
            "password",
        )


class RegisterUserMutation(graphene.Mutation):
    """Mutation to register a new user."""

    class Arguments:
        """Input arguments for our mutation."""

        phone_number = graphene.String(required=True)
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    user = graphene.Field(UserProfileType)

    @classmethod
    def mutate(
        cls, root, info, phone_number, first_name, last_name, email, password
    ):
        """Register a user."""
        user = UserProfile.objects.create(
            phone_number=phone_number,
            email=email,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save()

        return RegisterUserMutation(user=user)


class UpdateUserProfileMutation(graphene.Mutation):
    """Mutation to update a user's profile."""

    class Arguments:
        """Input arguments for our mutation."""

        phone_number = graphene.String()
        first_name = graphene.String()
        last_name = graphene.String()
        email = graphene.String()

    user = graphene.Field(UserProfileType)

    @classmethod
    def mutate(cls, root, info, phone_number, first_name, last_name, email):
        """Update a user's profile."""
        if not info.context.user.is_authenticated:
            return Exception("Log in first to update your user profile")

        user_pk = info.context.user.pk
        user = UserProfile.objects.get(pk=user_pk)
        if phone_number is not None:
            user.phone_number = phone_number

        if first_name is not None:
            user.first_name = first_name

        if last_name is not None:
            user.last_name = last_name

        if email is not None:
            user.email = email

        user.save()

        return UpdateUserProfileMutation(user=user)


class ChangePasswordMutation(graphene.Mutation):
    """Change password mutation."""

    class Arguments:
        """Input arguments for our mutation."""

        old_password = graphene.String(required=True)
        new_password = graphene.String(required=True)

    user = graphene.Field(UserProfileType)

    @classmethod
    def mutate(cls, root, info, old_password, new_password):
        """Update a user's password."""
        if not info.context.user.is_authenticated:
            return Exception("User is not logged in")

        user = info.context.user
        verify = check_password(old_password, user.password)
        if not verify:
            return Exception("Your passwords did not match. Please try again")

        user.set_password(new_password)
        user.save()

        return ChangePasswordMutation(user=user)


class Query(graphene.ObjectType):
    """User profiles queries."""

    users = graphene.List(UserProfileType)

    def resolve_users(root, info):
        """Users query resolver."""
        return UserProfile.objects.all()


class Mutation(graphene.ObjectType):
    """User profile mutation object types."""

    register_user = RegisterUserMutation.Field()
    update_user = UpdateUserProfileMutation.Field()
    change_password = ChangePasswordMutation.Field()
    login_user = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()
