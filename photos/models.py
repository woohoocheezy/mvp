from django.db import models
from commons.models import CommonModel


class Photo(CommonModel):

    """Photo Model Definition"""

    file = models.URLField()

    item = models.ForeignKey(
        "items.Item",
        null=True,
        related_name="photos",
        on_delete=models.SET_NULL,
    )
