from rest_framework.serializers import ModelSerializer, BooleanField
from .models import CustomUser


class CustomUserSerializer(ModelSerializer):
    chat_notification_allowed = BooleanField(required=False, default=True)
    marketing_notification_allowed = BooleanField(required=False, default=True)

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
