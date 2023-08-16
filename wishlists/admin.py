from django.contrib import admin
from .models import Wishlist, WishlistItem


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("id", "user")


@admin.register(WishlistItem)
class WishlistItemAdmin(admin.ModelAdmin):
    list_display = ("id", "wishlist", "item", "added_at")
