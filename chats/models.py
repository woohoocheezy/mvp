from django.db import models
from commons.models import CommonModel
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from uuid import uuid4


class Chat(CommonModel):
    chat_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
    )

    last_chat = models.TextField(null=True, blank=True)
    last_chat_date = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=255)

    # Foreign Key relationship with the User model for seller and buyer
    seller = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="seller_chats",
    )

    buyer = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="buyer_chats",
    )

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="chats",
    )
    object_id = models.UUIDField()

    item = GenericForeignKey(
        "content_type",
        "object_id",
    )


class Message(CommonModel):
    class MessageTypeChoices(models.TextChoices):
        TEXT = ("text", "Text")
        IMAGE = ("image", "Image")
        AUCTION_NOT_SELL = ("auctionNotSell", "Auction Not Sell")

    message_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
    )

    is_read = models.BooleanField(default=False)
    text = models.TextField()
    type = models.CharField(
        max_length=20, choices=MessageTypeChoices.choices, null=False, default="text"
    )
    image = models.URLField(null=True)
    time_sent = models.DateTimeField(auto_now_add=True)

    # Foreign key relationship with the User model about sender and receiver
    sender_user_id = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="sent_messages",
        null=True,
    )

    receiver_user_id = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="recieved_messages",
        null=True,
    )  # The fcm token of reciver can be obtained by ORM of CustomUser

    # Foreign key relationship with the Chat model
    chat = models.ForeignKey(
        Chat,
        on_delete=models.SET_NULL,
        related_name="messages",
        null=True,
    )
