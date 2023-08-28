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
        "user_id",
        "buy_user_id",
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
    )


@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = (
        "item_uuid",
        "item_name",
        "user_id",
        "buy_user_id",
        "is_sold",
        "is_deleted",
        "used_years",
        "manufactured_date",
        "is_manufactured",
        "description",
        "category",
        "location",
        "deadline",
        "lowest_price",
    )
