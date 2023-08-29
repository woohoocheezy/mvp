from django.contrib import admin
from .models import Wishlist

# from django.contrib.contenttypes.admin import GenericTabularInline


# class WishlistItemRelationInline(GenericTabularInline):
#     model = WishlistItemRelation
#     extra = 1


# @admin.register(Wishlist)
# class WishlistAdmin(admin.ModelAdmin):
#     class Meta:
#         verbose_name = "찜하기"
#         verbose_name_plural = "찜하기"


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    list_display = ("wishlist_uuid", "user_id", "name", "created_at", "updated_at")
    search_fields = ("wishlist_uuid", "user_id", "name")
    list_per_page = 20
    readonly_fields = ("wishlist_uuid", "created_at", "updated_at")
