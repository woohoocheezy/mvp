from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
)
from photos.serializers import PhotoSerializer
from .models import FixedPriceItem, AuctionItem
from wishlists.models import Wishlist
from django.contrib.contenttypes.models import ContentType


class FixedPriceItemListWishSerializer(ModelSerializer):
    """Serializer Definition for FixedPriceItem List(wishlist)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = (
            "item_name",
            "photo",
            "is_negotiable",
            "is_sold",
            "price",
            "location",
            "item_uuid",
            "is_liked",
            "count_liked",
            "is_deleted",
        )

    def get_photo(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(
            object_id=item.pk, is_thumbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            fixed_price_items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(fixed_price_items__pk=item.pk).count()


class FixedPriceItemListSerializer(ModelSerializer):
    """Serializer Definition for Item List(store)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = (
            "item_name",
            "photo",
            "is_negotiable",
            "is_sold",
            "price",
            "location",
            "item_uuid",
            "is_liked",
            "is_deleted",
            "count_liked",
            "user_id",
        )

    def get_photo(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(
            object_id=item.pk, is_thumbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            fixed_price_items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(fixed_price_items__pk=item.pk).count()


class FixedPriceItemDetailSerializer(ModelSerializer):
    photos = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = "__all__"

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("uid"),
            fixed_price_items__pk=item.pk,
        ).exists()

    def get_photos(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(object_id=item.pk).order_by(
            "-is_thumbnail"
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data if photo_serializer.data else None

    def get_count_liked(self, item):
        return Wishlist.objects.filter(fixed_price_items__pk=item.pk).count()


class AuctionItemListWishSerializer(ModelSerializer):
    """Serializer Definition for Auction Item List(wishlist)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_bids = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = (
            "item_name",
            "photo",
            "deadline",
            "is_sold",
            "lowest_price",
            "location",
            "item_uuid",
            "is_liked",
            "count_liked",
            "is_deleted",
            "count_bids",
        )

    def get_photo(self, auction_item):
        content_type = ContentType.objects.get_for_model(auction_item)
        photos_queryset = content_type.photos.filter(
            object_id=auction_item.pk, is_thunbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            auction_items__pk=auction_item.pk,
        ).exists()

    def get_count_liked(self, auction_item):
        return Wishlist.objects.filter(auction_items__pk=auction_item.pk).count()

    def get_count_bids(self, auction_item):
        return auction_item.biddings.count()


class AuctionItemListSerializer(ModelSerializer):
    """Serializer Definition for Auction Item List(store)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_bids = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = (
            "item_name",
            "photo",
            "deadline",
            "is_sold",
            "lowest_price",
            "location",
            "item_uuid",
            "is_liked",
            "is_deleted",
            "count_liked",
            "user_id",
            "count_bids",
        )

    def get_photo(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(
            object_id=item.pk, is_thumbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            auction_items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(auction_items__pk=item.pk).count()

    def get_count_bids(self, auction_item):
        return auction_item.biddings.count()


class AuctionItemDetailSerializer(ModelSerializer):
    photos = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_bids = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = "__all__"

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("uid"),
            auction_items__pk=auction_item.pk,
        ).exists()

    def get_photos(self, auction_item):
        content_type = ContentType.objects.get_for_model(auction_item)
        photos_queryset = content_type.photos.filter(
            object_id=auction_item.pk
        ).order_by("-is_thumbnail")
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data if photo_serializer.data else None

    def get_count_liked(self, auction_item):
        return Wishlist.objects.filter(auction_items__pk=auction_item.pk).count()

    def get_count_bids(self, auction_item):
        return auction_item.biddings.count()


class UserSoldSerializer(Serializer):

    """a serializer for user's 'sold' history that shows mixed models that inherit BaseItem"""

    item = SerializerMethodField()

    def get_item(self, item):
        if isinstance(item, FixedPriceItem):
            return FixedPriceItemListSerializer(
                item,
                context=self.context,
            ).data
        elif isinstance(item, AuctionItem):
            return AuctionItemListSerializer(
                item,
                context=self.context,
            ).data
