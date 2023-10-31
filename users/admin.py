from django.contrib import admin
from .models import CustomUser
import csv
from django.http import HttpResponse


def export_to_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="users.csv"'
    writer = csv.writer(response)
    fields = [
        "nick_name",
        "name",
        "sector",
        "user_type",
        "phone_number",
        "create_at",
        "chat_notification_allowed",
        "marketing_notification_allowed",
        "is_certificated",
        "is_deleted",
        "birth_date",
    ]
    writer.writerow(fields)
    queryset = queryset.order_by("create_at")
    for user in queryset:
        row = writer.writerow([getattr(user, field) for field in fields])
    return response


export_to_csv.short_description = "Export to CSV"


@admin.register(CustomUser)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "user_uuid",
        "nick_name",
        "user_type",
        "name",
        "create_at",
        "chat_notification_allowed",
        "marketing_notification_allowed",
        "is_certificated",
        "fcm_token",
        "is_deleted",
    )
    list_filter = (
        "user_type",
        "chat_notification_allowed",
        "marketing_notification_allowed",
        "is_certificated",
    )
    actions = [export_to_csv]
