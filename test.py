from wishlists.models import Wishlist
from photos.models import Photo
from photos.serializers import PhotoSerializer
from items.models import FixedPriceItem, AuctionItem


from django.contrib.contenttypes.models import ContentType


# def migration_test():
#     print(FixedPriceItem.objects.all())
#     for wishlist in Wishlist.objects.all():
#         new_wishlist = TempWishlist()
#         new_wishlist.save()
#         # print(f"[{wishlist.user_id}]")
#         # print("items: ", wishlist.items.all())
#         # print("BaseItems: ", FixedPriceItem.objects.filter(user_id=wishlist.user_id))
#         new_wishlist.items.set(FixedPriceItem.objects.filter(user_id=wishlist.user_id))


# def photo_migration_test():
#     for photo in Photo.objects.all():
#         if photo.item:
#             print(photo.item)
#             print(photo.item.user_id)

#     content_type = (ContentType.objects.get_for_model(FixedPriceITem),)
#     object_id = (ContentType.objects.get(user_id=photo.item.user_id),)


def photo_test():
    auction_items = AuctionItem.objects.all()

    for item in auction_items:
        print(item, end=" ")
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        # print(photos_queryset)
        print(photos_queryset[0], photos_queryset[0].is_thumbnail, end=" ")
        photo = photos_queryset[0]
        photo.is_thumbnail = True
        photo.save()
        print(photos_queryset[0].is_thumbnail)

    fixed_items = FixedPriceItem.objects.all()

    for item in fixed_items:
        print(item, end=" ")
        content_type = ContentType.objects.get_for_model(item)
        photos_queryset = content_type.photos.filter(object_id=item.pk)
        # print(photos_queryset)
        print(photos_queryset[0], photos_queryset[0].is_thumbnail, end=" ")
        photo = photos_queryset[0]
        photo.is_thumbnail = True
        photo.save()
        print(photos_queryset[0].is_thumbnail)
