from django.db import models
from commons.models import CommonModel
from items.models import Item


class Wishlist(CommonModel):
    user_id = models.TextField()
    name = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )
    items = models.ManyToManyField(
        Item,
        related_name="wishlists",
    )
    # likes = models.ManyToManyField(related_name="liked_items", blank=True)
