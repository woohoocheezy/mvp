from rest_framework.serializers import (
    ModelSerializer,
    UUIDField,
    SerializerMethodField,
    StringRelatedField,
)
from .models import Chat, Message
from items.models import FixedPriceItem
from users.models import CustomUser
from photos.serializers import PhotoSerializer
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatDetailSerializer(ModelSerializer):
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
            defaults={
                **validated_data,  # use other fields for chat creation if it doesn't exist yet.
                "seller_active": True,
                "buyer_active": True,
            },
        )

        return chat


class MessageSerializer(ModelSerializer):
    """sumary_line

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    sender_user_id = StringRelatedField()
    receiver_user_id = StringRelatedField()

    class Meta:
        model = Message
        fields = [
            "message_uuid",
            "is_read",
            "text",
            "type",
            "image",
            "time_sent",
            "sender_user_id",
            "receiver_user_id",
        ]


class ChatListSerializer(ModelSerializer):
    """The list of chat rooms

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    item_name = SerializerMethodField()
    item_uuid = SerializerMethodField()
    last_chat = SerializerMethodField()
    last_chat_date = SerializerMethodField()
    other_user_profile = SerializerMethodField()
    other_user_nickname = SerializerMethodField()
    product_image = SerializerMethodField()
    unread_count = SerializerMethodField()

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
            "other_user_profile",
            "other_user_nickname",
            "product_image",
            "unread_count",
        ]

    def get_item_name(self, chat):
        return chat.item.item_name

    def get_item_uuid(self, chat):
        return chat.item.item_uuid

    def get_last_chat(self, chat):
        last_message = chat.messages.order_by("-time_sent").first()
        if last_message is not None:
            return last_message.text
        else:
            # logging.info(f"{chat.content_type} & {chat.object_id} & {chat.item}")
            # logging.info(type(chat.item))
            if type(chat.item) == FixedPriceItem:
                return "대화를 시작해보세요"
            else:  # The case of AuctionItem
                if chat.item.is_overdue and chat.item.is_bidded:
                    return "경매가 완료되어, 판매자분과 최고 입찰자분이 매칭되었어요!"
                else:
                    return "경매가 완료되었지만, 입찰자가 없어요"

    def get_last_chat_date(self, chat):
        last_message = chat.messages.order_by("-time_sent").first()

        if last_message is not None:
            return timezone.localtime(last_message.time_sent)
        else:
            return timezone.localtime(chat.created_at)

    def get_other_user_profile(self, chat):
        request_user = self.context["request"].user
        other_user = chat.seller if request_user != chat.seller else chat.buyer

        return other_user.profile_image_url

    def get_other_user_nickname(self, chat):
        request_user = self.context["request"].user
        other_user = chat.seller if request_user != chat.seller else chat.buyer

        return other_user.nick_name

    def get_product_image(self, chat):
        content_type = ContentType.objects.get_for_model(chat.item)
        photos_queryset = content_type.photos.filter(
            object_id=chat.item.pk, is_thumbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_unread_count(self, chat):
        request_user = self.context["request"].user
        unread_messages = chat.messages.filter(
            receiver_user_id=request_user, is_read=False
        )

        return unread_messages.count()
