from rest_framework.serializers import ModelSerializer
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"


class BlockedUserSerailizer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            "user_uuid",
            "nick_name",
            "name",
        )
