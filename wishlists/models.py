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
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    fixed_price_items = models.ManyToManyField(
        FixedPriceItem,
        related_name="wishlists",
    )

    auction_items = models.ManyToManyField(
        AuctionItem,
        related_name="wishlists",
    )
