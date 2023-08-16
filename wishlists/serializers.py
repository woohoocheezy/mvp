from rest_framework import serializers
from items.serializers import ItemListWishSerializer
from .models import Wishlist


class WishlistSerializer(serializers.ModelSerializer):
    items = ItemListWishSerializer(many=True, read_only=True)

    class Meta:
        model = Wishlist
        fields = (
            "id",
            "user",
            "name",
            "items",
        )
