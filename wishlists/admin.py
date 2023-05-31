from django.contrib import admin
from .models import Wishlist


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    class Meta:
        verbose_name = "찜하기"
        verbose_name_plural = "찜하기"
