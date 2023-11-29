from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import exceptions, serializers
from users.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    phone_number = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        self.fields.pop("password", None)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token["user_phone_number"] = user.phone_number
        return token

    def validate(self, attrs):
        # retrieve 'user_id' provided by client
        phone_number = attrs.get("phone_number")

        if not phone_number:
            raise exceptions.AuthenticationFailed(
                {"phone_number": "This field is required."}
            )

        try:
            # retrieve the user with provided 'user_id'
            user = CustomUser.objects.get(phone_number=phone_number)

        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                {"Authentication Failed": "No user found with provied phone_number."}
            )

        # save the valid user
        self.user = user
        self.user.is_deleted = False
        self.user.save()

        # get a JWT token
        refresh = self.get_token(self.user)
        # print(phone_number)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user_phone_number": self.user.phone_number,
        }
        # print(phone_number)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        data["access"] = str(refresh.access_token)
        return data


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
