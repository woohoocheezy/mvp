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

    product = GenericForeignKey(
        "content_type",
        "object_id",
    )


class Message(CommonModel):
    message_uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        editable=False,
        unique=True,
    )

    is_read = models.BooleanField(default=False)
    text = models.TextField()
    time_sent = models.DateTimeField(auto_now_add=True)

    # Foreign key relationship with the User model
    sender_user_id = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="sent_messages",
    )

    receiver_user_id = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="recieved_messages",
    )

    chat_room = models.ForeignKey(
        Chat,
        on_delete=models.CASCADE,
        related_name="messages",
    )
