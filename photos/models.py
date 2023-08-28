from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from commons.models import CommonModel
import uuid


class TempPhoto(CommonModel):

    """Photo Model Definition"""

    photo_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    file = models.URLField()
    item_uuid = models.BigIntegerField(null=True)

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
    )
    object_id = models.UUIDField()

    item = GenericForeignKey(
        "content_type",
        "object_id",
    )


# class Photo(CommonModel):

#     """Photo Model Definition"""

#     file = models.URLField()

#     item = models.ForeignKey(
#         "items.Item",
#         null=True,
#         blank=True,
#         related_name="photos",
#         on_delete=models.SET_NULL,
#     )
