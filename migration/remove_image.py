from django.contrib.contenttypes.models import ContentType
from photos.models import Photo
from items.models import FixedPriceItem, AuctionItem


def removeImage():
    fixed_items = FixedPriceItem.objects.filter(is_deleted=True)
    content_type = ContentType.objects.get_for_model(FixedPriceItem)

    for item in fixed_items:
        print(item.item_name)
        photos = Photo.objects.filter(
            content_type=content_type, object_id=item.item_uuid
        )

        for photo in photos:
            print(photo.file)
