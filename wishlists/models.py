from django.db import models
from commons.models import CommonModel
from items.models import Item
from django.utils import timezone


class Wishlist(CommonModel):
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
    items = models.ManyToManyField(
        Item,
        related_name="wishlists",
    )


class WishlistItem(models.Model):
    wishlist = models.ForeignKey(Wishlist, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("wishlist", "item")
