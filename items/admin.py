from django.contrib import admin
from .models import FixedPriceItem, AuctionItem


# @admin.register(Item)
# class ItemAdmin(admin.ModelAdmin):
#     list_display = (
#         "id",
#         "item_name",
#         "price",
#         "is_sold",
#         "is_deleted",
#         "user_id",
#         "used_years",
#         "category",
#         "description",
#     )
#     list_filter = ("price", "category", "used_years", "location")
#     search_fields = ("item_name", "item_description")
#     ordering = ("id",)


@admin.register(FixedPriceItem)
class FixedPriceItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_uuid",
        "item_name",
        "user",
        "buy_user",
        "is_sold",
        "is_deleted",
        "used_years",
        "manufactured_date",
        "is_manufactured",
        "description",
        "category",
        "location",
        "price",
        "is_negotiable",
        "created_at",
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
        "used_years",
        "manufactured_date",
        "is_manufactured",
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
        "used_years",
    )
