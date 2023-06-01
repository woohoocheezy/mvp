from rest_framework.serializers import ModelSerializer, SerializerMethodField
from photos.serializers import PhotoSerializer
from datetime import date
from .models import Item
from wishlists.models import Wishlist

# from photos.serailizer import PhotoSerializer


class ItemListWishSerializer(ModelSerializer):
    """Serializer Definition for Item List(store)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    dday = SerializerMethodField()

    class Meta:
        model = Item

        # 찜
        fields = (
            "item_name",
            "photo",  # 대표사진
            "is_negotiable",
            "is_sold",
            "price",
            "location",
            "pk",
            "is_liked",
            "count_liked",
            "is_deleted",
            "dday",
        )

    def get_photo(self, item):
        photo_serializer = PhotoSerializer(item.photos.all(), many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=item.pk,
        ).exists()

    def get_count_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(items__pk=item.pk).count()

    def get_dday(self, item):
        if item.dday_date:
            delta = item.dday_date - date.today()
            return delta.days
        return None


class ItemListSerializer(ModelSerializer):
    """Serializer Definition for Item List(store)"""

    # 대표 이미지만 불러 오는 지 확인해야됨
    photo = SerializerMethodField()
    is_liked = SerializerMethodField()
    dday = SerializerMethodField()
    count_liked = SerializerMethodField()

    class Meta:
        model = Item

        fields = (
            "item_name",
            "photo",  # 대표사진
            "is_negotiable",
            "is_sold",
            "price",
            "location",
            "pk",
            "is_liked",
            "is_deleted",
            "dday",
            "count_liked",
        )

    def get_photo(self, item):
        photo_serializer = PhotoSerializer(item.photos.all(), many=True)

        return photo_serializer.data[0] if photo_serializer.data else None

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("user_id"),
            items__pk=item.pk,
        ).exists()

    def get_dday(self, item):
        if item.dday_date:
            delta = item.dday_date - date.today()
            return delta.days
        return None

    def get_count_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(items__pk=item.pk).count()


class ItemDetailSerializer(ModelSerializer):
    photos = PhotoSerializer(many=True, read_only=True)
    is_liked = SerializerMethodField()
    count_liked = SerializerMethodField()
    dday = SerializerMethodField()

    class Meta:
        model = Item

        fields = "__all__"

        # fields = (
        #     "item_name",
        #     "user_ID",
        #     # "photos",
        #     "is_negotiable",
        #     "is_liked",
        #     "is_sold",
        #     "price",
        #     "used_years",
        #     "manufactured_date",
        #     "warranty_date",
        #     "description",
        #     "category",
        #     "dday_date",
        #     "location",
        # )

    def get_is_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(
            user_id=request.user.get("uid"),
            items__pk=item.pk,
        ).exists()

    def get_dday(self, item):
        if item.dday_date:
            delta = item.dday_date - date.today()
            return delta.days
        return None

    def get_count_liked(self, item):
        request = self.context["request"]
        return Wishlist.objects.filter(items__pk=item.pk).count()
