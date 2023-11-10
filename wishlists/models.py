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

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="wishlists",
    )

    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    fixed_price_items = models.ManyToManyField(
        FixedPriceItem,
        related_name="wishlists",
        blank=True,
    )

    auction_items = models.ManyToManyField(
        AuctionItem,
        related_name="wishlists",
        blank=True,
    )
