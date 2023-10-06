from rest_framework.serializers import ModelSerializer, UUIDField, SerializerMethodField
from .models import Chat, Message
from items.models import FixedPriceItem
from users.models import CustomUser
from django.contrib.contenttypes.models import ContentType


class ChatCreateSerializer(ModelSerializer):
    item_uuid = UUIDField(write_only=True)
    seller = UUIDField(write_only=True)

    class Meta:
        model = Chat
        fields = [
            "seller",
            "buyer",
            "item_uuid",
        ]

    def create(self, validated_data):
        user = self.context["request"].user

        item_uuid = validated_data.pop("item_uuid")
        item = FixedPriceItem.objects.get(item_uuid=item_uuid)

        seller_id = validated_data.pop("seller")
        seller = CustomUser.objects.get(user_uuid=seller_id)

        content_type = ContentType.objects.get_for_model(item)

        chat, created = Chat.objects.get_or_create(
            seller=seller,
            buyer=user,
            content_type=content_type,
            object_id=item.item_uuid,
            title=item.item_name,
            defaults=validated_data,  # use other fields for chat creation if it doesn't exist yet.
        )

        return chat


class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"


class ChatMessageSerailizer(ModelSerializer):
    """The messages list of the specific chat room

    Keyword arguments:
    argument -- none
    Return: the list of messages
    """

    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = Chat
        fields = [
            "chat_uuid",
            "last_chat",
            "last_chat_date",
            "title",
            "seller",
            "buyer",
            "item",
        ]


class ChatListSerializer(ModelSerializer):
    """The list of chat rooms

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    item_name = SerializerMethodField()
    item_uuid = SerializerMethodField()

    class Meta:
        model = Chat
        fields = [
            "chat_uuid",
            "last_chat",
            "last_chat_date",
            "title",
            "buyer",
            "seller",
            "item_name",
            "item_uuid",
        ]

    def get_item_name(self, chat):
        print("chat_item_name: ", chat.item.item_name)
        return chat.item.item_name

    def get_item_uuid(self, chat):
        return chat.item.item_uuid


# class FixedPriceChatSerializer(ModelSerializer):
#     items =
#     class meta:
#         model = Chat

#         fields = [
#             "seller",
#             "buyer",
#             "item",
#         ]
