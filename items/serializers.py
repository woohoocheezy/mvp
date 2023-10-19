from rest_framework.serializers import (
    ModelSerializer,
    SerializerMethodField,
    Serializer,
)
from photos.serializers import PhotoSerializer
from .models import FixedPriceItem, AuctionItem
from datetime import date
from biddings.models import Bidding
from wishlists.models import Wishlist
from chats.models import Chat
from django.contrib.contenttypes.models import ContentType


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class FixedPriceItemListWishSerializer(ModelSerializer):
    """Serializer Definition for FixedPriceItem List(wishlist)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_chats = SerializerMethodField()

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
            "count_chats",
        )

    def get_count_chats(self, item):
        return Chat.objects.filter(object_id=item.pk).count()

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
            user=request.user,
            fixed_price_items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(fixed_price_items__pk=item.pk).count()


class FixedPriceItemListSerializer(ModelSerializer):
    """Serializer Definition for Item List(store)"""

    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_chats = SerializerMethodField()

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
            "count_chats",
        )

    def get_count_chats(self, item):
        return Chat.objects.filter(object_id=item.pk).count()

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
            user=request.user,
            fixed_price_items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(fixed_price_items__pk=item.pk).count()


class FixedPriceItemDetailSerializer(ModelSerializer):
    photos = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    count_chats = SerializerMethodField()
    user_profile = SerializerMethodField()
    user_nickname = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = "__all__"

    def get_count_chats(self, item):
        return Chat.objects.filter(object_id=item.pk).count()

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user=request.user,
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

    def get_user_profile(self, item):
        return item.user.profile_image_url

    def get_user_nickname(self, item):
        return item.user.nick_name


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
            object_id=auction_item.pk, is_thumbnail=True
        )
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user=request.user,
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
            user=request.user,
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
    user_profile = SerializerMethodField()
    user_nickname = SerializerMethodField()
    is_bid_possible = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = "__all__"

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user=request.user,
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

    def get_user_profile(self, item):
        return item.user.profile_image_url

    def get_user_nickname(self, item):
        return item.user.nick_name

    def get_is_bid_possible(self, item):
        user = self.context["request"].user

        if (item.deadline < date.today()) is True:
            return False

        if Bidding.objects.filter(
            user_id=user.user_uuid, auction_item__pk=item.item_uuid
        ).exists():
            return False

        return True


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
