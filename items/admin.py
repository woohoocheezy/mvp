from django.contrib import admin
from .models import FixedPriceItem, AuctionItem


@admin.register(FixedPriceItem)
class FixedPriceItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_uuid",
        "item_name",
        "user",
        "buy_user",
        "is_sold",
        "is_deleted",
        "description",
        "category",
        "location",
        "price",
        "created_at",
        "used_period",
    )


@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_uuid",
        "item_name",
        "user",
        "buy_user",
        "is_overdue",
        "deadline",
        "is_bidded",
        "is_sold",
        "is_deleted",
        "description",
        "category",
        "location",
        "lowest_price",
        "created_at",
    )
    list_filter = (
        "is_overdue",
        "is_bidded",
        "is_sold",
        "is_deleted",
    )
