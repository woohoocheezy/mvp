from rest_framework import serializers
from items.serializers import (
    FixedPriceItemListWishSerializer,
    AuctionItemListWishSerializer,
)
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = (
            "wishlist_uuid",
            "name",
        )


class FixedPriceItemWishlistSerializer(serializers.ModelSerializer):
    fixed_price_items = FixedPriceItemListWishSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = (
            "wishlist_uuid",
            "name",
            "fixed_price_items",
        )


class AuctionItemWishlistSerializer(serializers.ModelSerializer):
    auction_items = AuctionItemListWishSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = (
            "wishlist_uuid",
            "name",
            "auction_items",
        )
