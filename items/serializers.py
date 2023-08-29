from rest_framework.serializers import ModelSerializer, SerializerMethodField
from photos.serializers import PhotoSerializer
from datetime import date
from .models import FixedPriceItem, AuctionItem
from wishlists.models import Wishlist
from django.contrib.contenttypes.models import ContentType


class FixedPriceItemListWishSerializer(ModelSerializer):
    """Serializer Definition for FixedPriceItem List(wishlist)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    # dday = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        # 찜
        fields = (
            "item_name",
            "photo",  # 대표사진
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
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        return Wishlist.objects.filter(items__pk=item.pk).count()

    # def get_dday(self, item):
    #     if item.dday_date:
    #         delta = item.dday_date - date.today()
    #         return delta.days
    #     return None


class FixedPriceItemListSerializer(ModelSerializer):
    """Serializer Definition for Item List(store)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    # dday = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = (
            "item_name",
            "photo",  # 대표사진
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
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=item.pk,
        ).exists()

    # def get_dday(self, item):
    #     if item.dday_date:
    #         delta = item.dday_date - date.today()
    #         return delta.days
    #     return None

    def get_count_liked(self, item):
        return Wishlist.objects.filter(items__pk=item.pk).count()


class FixedPriceItemDetailSerializer(ModelSerializer):
    photos = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    # dday = SerializerMethodField()

    class Meta:
        model = FixedPriceItem

        fields = "__all__"

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("uid"),
            items__pk=item.pk,
        ).exists()

    def get_photos(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data if photo_serializer.data else None

    # def get_dday(self, item):
    #     if item.dday_date:
    #         delta = item.dday_date - date.today()
    #         return delta.days
    #     return None

    def get_count_liked(self, item):
        return Wishlist.objects.filter(items__pk=item.pk).count()


class AuctionItemListWishSerializer(ModelSerializer):
    """Serializer Definition for Auction Item List(wishlist)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    # dday = SerializerMethodField()

    class Meta:
        model = AuctionItem

        # 찜
        fields = (
            "item_name",
            "photo",  # 대표사진
            "deadline",
            "is_sold",
            "lowest_price",
            "location",
            "item_uuid",
            "is_liked",
            "count_liked",
            "is_deleted",
            # "dday",
        )

    def get_photo(self, auction_item):
        content_type = ContentType.objects.get_for_model(auction_item)
        photos_queryset = content_type.photos.filter(object_id=auction_item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=auction_item.pk,
        ).exists()

    def get_count_liked(self, auction_item):
        return Wishlist.objects.filter(items__pk=auction_item.pk).count()

    # def get_dday(self, item):
    #     if item.dday_date:
    #         delta = item.dday_date - date.today()
    #         return delta.days
    #     return None


class AuctionItemListSerializer(ModelSerializer):
    """Serializer Definition for Auction Item List(store)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    # dday = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = (
            "item_name",
            "photo",  # 대표사진
            "deadline",
            "is_sold",
            "lowest_price",
            "location",
            "item_uuid",
            "is_liked",
            "is_deleted",
            "count_liked",
            "user_id",
        )

    def get_photo(self, item):
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=item.pk,
        ).exists()

    # def get_dday(self, item):
    #     if item.dday_date:
    #         delta = item.dday_date - date.today()
    #         return delta.days
    #     return None

    def get_count_liked(self, item):
        return Wishlist.objects.filter(items__pk=item.pk).count()


class AuctionItemDetailSerializer(ModelSerializer):
    photos = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    dday = SerializerMethodField()

    class Meta:
        model = AuctionItem

        fields = "__all__"

    def get_is_liked(self, auction_item):
        request = self.context["request"]

        return Wishlist.objects.filter(
            user_id=request.user.get("uid"),
            items_pk=auction_item.pk,
        ).exists()

    def get_count_liked(self, auction_item):
        content_type = ContentType.objects.get_for_model(auction_item)
        photos_queryset = content_type.photos.filter(object_id=auction_item.pk)
        photo_serializer = PhotoSerializer(photos_queryset, many=True)

        return photo_serializer.data if photo_serializer.data else None

    def get_photos(self, auction_item):
        return Wishlist.objects.filter(items_pk=auction_item.pk).count()
