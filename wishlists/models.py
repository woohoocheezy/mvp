from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from commons.models import CommonModel
from items.models import BaseItem
import uuid


class TempWishlist(CommonModel):
    wishlist_uuid = models.UUIDField(
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user_id = models.TextField()
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    items = GenericRelation(
        "WishlistItemRelation",
        related_query_name="wishlist",
    )


class WishlistItemRelation(models.Model):
    wishlist = models.ForeignKey(TempWishlist, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.CharField(max_length=50)
    base_item = GenericForeignKey("content_type", "object_id")


# class Wishlist(CommonModel):
#     user_id = models.TextField()
#     name = models.CharField(
#         max_length=150,
#         null=True,
#         blank=True,
#     )
#     items = models.ManyToManyField(
#         Item,
#         related_name="wishlists",
#     )
