from django.db import models
from commons.models import CommonModel
from items.models import FixedPriceItem, AuctionItem
import uuid


class Wishlist(CommonModel):
    wishlist_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user_id = models.TextField()
    temp_user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="wishlists",
        null=True,
    )  # need to remove on the step 4 after migration

    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    fixed_price_items = models.ManyToManyField(
        FixedPriceItem,
        related_name="wishlists",
    )  # need to remove on the step 4 after migration

    auction_items = models.ManyToManyField(
        AuctionItem,
        related_name="wishlists",
    )  # need to remove on the step 4 after migration


class WishlistFixedPriceItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    item = models.ForeignKey(FixedPriceItem, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("wishlist", "item")


class WishlistAuctionItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("wishlist", "item")
