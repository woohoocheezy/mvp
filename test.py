from wishlists.models import Wishlist, TempWishlist
from photos.models import Photo
from items.models import FixedPriceItem

from django.contrib.contenttypes.models import ContentType


def migration_test():
    print(FixedPriceItem.objects.all())
    for wishlist in Wishlist.objects.all():
        new_wishlist = TempWishlist()
        new_wishlist.save()
        # print(f"[{wishlist.user_id}]")
        # print("items: ", wishlist.items.all())
        # print("BaseItems: ", FixedPriceItem.objects.filter(user_id=wishlist.user_id))
        new_wishlist.items.set(FixedPriceItem.objects.filter(user_id=wishlist.user_id))


def photo_migration_test():
    for photo in Photo.objects.all():
        if photo.item:
            print(photo.item)
            print(photo.item.user_id)

    content_type = (ContentType.objects.get_for_model(FixedPriceITem),)
    object_id = (ContentType.objects.get(user_id=photo.item.user_id),)
