from django.db import models
from commons.models import CommonModel
import uuid


class Bidding(CommonModel):

    """Bidding Model Definition for Auction"""

    bidding_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user_id = models.TextField()
    bidding_price = models.PositiveIntegerField()

    auction_item = models.ForeignKey(
        "items.AuctionItem",
        related_name="biddings",
        null=True,
        on_delete=models.SET_NULL,
    )
