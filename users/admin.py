from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_uuid",
        "temp_user_id",
        "nick_name",
        "user_type",
        "name",
        "chat_notification_allowed",
        "marketing_notification_allowed",
        "is_certificated",
        "fcm_token",
    )
    list_filter = (
        "user_type",
        "chat_notification_allowed",
        "marketing_notification_allowed",
        "is_certificated",
    )
