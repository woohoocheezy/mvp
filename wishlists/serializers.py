from rest_framework import serializers
from items.serializers import FixedPriceItemListWishSerializer
from .models import TempWishlist


class WishlistSerializer(serializers.ModelSerializer):
    items = FixedPriceItemListWishSerializer(many=True, read_only=True)

    class Meta:
        model = TempWishlist
        fields = ("id", "name", "items")
