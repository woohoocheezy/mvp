from rest_framework import serializers
from items.serializers import FixedPriceItemListWishSerializer
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    items = FixedPriceItemListWishSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = ("wishlist_uuid", "name", "items")
