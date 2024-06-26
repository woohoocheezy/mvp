from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from commons.models import CommonModel
import uuid


class Photo(CommonModel):

    """Photo Model Definition"""

    photo_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    file = models.URLField()

    content_type = models.ForeignKey(
        ContentType,
        on_delete=models.CASCADE,
        related_name="photos",
    )
    object_id = models.UUIDField()

    item = GenericForeignKey(
        "content_type",
        "object_id",
    )

    is_thumbnail = models.BooleanField(default=False)
