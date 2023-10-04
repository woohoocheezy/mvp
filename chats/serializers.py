from rest_framework import serializers
from .models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = [
            "chat_uuid",
            "create_at",
            "last_chat",
            "last_chat_date",
            "title",
            "seller",
            "buyer",
            "product",
        ]


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = [
            "message_uuid",
            "is_read",
            "text",
            "time_sent",
            "sender_user_id",
            "receiver_user_id",
            "chat_room",
        ]
