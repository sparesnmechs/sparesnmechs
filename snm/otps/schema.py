"""Otps app GraphQL schema."""
import graphene
from django.core.exceptions import ObjectDoesNotExist

from snm.otps.models import Otp
from snm.otps.utilities import generateOTP, verifyOTP
from snm.userprofiles.models import UserProfile


class GenerateOTPMutation(graphene.Mutation):
    """Generate phone OTP."""

    class Arguments:
        """Input arguments for our mutation."""

        phone_number = graphene.String(required=True)

    otp = graphene.String()

    @classmethod
    def mutate(cls, root, info, phone_number):
        """Geneate and save the OTP."""
        user = UserProfile.objects.get(phone_number=phone_number)
        if user is None:
            return Exception("can't send OTP to a number which does not exist")

        try:
            otp_model = Otp.objects.get(phone_number=phone_number)
        except ObjectDoesNotExist:
            otp_model = Otp.objects.create(phone_number=phone_number)

        otp = generateOTP()
        otp_model.code = otp
        verified = otp_model.is_verified
        if verified:
            verified = False

        otp_model.save()

        # TODO: Send an SMS with the OTP

        return GenerateOTPMutation(otp=otp)


class VerifyOTPMutation(graphene.Mutation):
    """Verify a given OTP."""

    class Arguments:
        """Input arguments for our mutation."""

        otp = graphene.String(required=True)

    response = graphene.String()

    @classmethod
    def mutate(cls, root, info, otp):
        """Verify a given OTP."""
        response = verifyOTP(otp)

        return VerifyOTPMutation(response=response)


class Query(graphene.ObjectType):
    """OTP query object."""

    pass


class Mutation(graphene.ObjectType):
    """OTP mutation objects."""

    generate_otp = GenerateOTPMutation.Field()
    verify_otp = VerifyOTPMutation.Field()
