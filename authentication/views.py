from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import exceptions, serializers
from users.models import CustomUser


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    phone_number = serializers.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop("username", None)
        self.fields.pop("password", None)

    # @staticmethod
    def validate(self, attrs):
        # retrieve 'user_id' provided by client
        phone_number = attrs.get("phone_number")

        if not phone_number:
            raise exceptions.AuthenticationFailed(
                {"phone_number": "This field is required."}
            )

        try:
            # retrieve the user with provided 'user_id'
            customUser = CustomUser.objects.get(phone_number=phone_number)
            user = customUser.user
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed(
                {"Authentication Failed": "No user found with provied phone_number."}
            )

        # save the valid user
        self.user = user

        print(phone_number)
        # print(self.user.name)

        # print("phone number:", self.user.phone_number)

        # get a JWT token
        refresh = self.get_token(self.user)
        print(phone_number)
        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
        }
        print(phone_number)

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
