from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "item_name",
        "price",
        "is_sold",
        "user_id",
        "used_years",
        "category",
        "description",
    )
    list_filter = ("price", "category", "used_years", "location")
    search_fields = ("item_name", "item_description")
    ordering = ("id",)
