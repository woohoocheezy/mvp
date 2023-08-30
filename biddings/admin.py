from django.contrib import admin
from .models import Bidding


@admin.register(Bidding)
class PhotoAdmin(admin.ModelAdmin):
    list_display = (
        "bidding_uuid",
        "user_id",
        "auction_item",
        "bidding_price",
    )
