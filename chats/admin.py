from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    list_display = (
        "chat_uuid",
        "title",
        "seller",
        "buyer",
        "content_type",
        "item",
    )


@admin.register(Message)
class MessageItemAdmin(admin.ModelAdmin):
    list_display = (
        "message_uuid",
        "is_read",
        "text",
        "type",
        "image",
        "time_sent",
        "sender_user_id",
        "receiver_user_id",
        "chat",
    )
