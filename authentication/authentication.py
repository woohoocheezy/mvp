from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken
from users.models import CustomUser


class CustomJWTAuthentication(JWTAuthentication):
    def get_user(self, validated_token):
        """
        Retrieve the user by user_phone_number.
        """
        user_phone_number = validated_token.get("user_phone_number", None)

        if user_phone_number is not None:
            try:
                custom_user = CustomUser.objects.get(phone_number=user_phone_number)
                user = custom_user
                return user
            except CustomUser.DoesNotExist:
                raise InvalidToken(
                    {
                        "Authentication Failed": "No user found with provied phone_number."
                    }
                )
        raise InvalidToken({"Authentication Failed": "A phone number is necessary."})
