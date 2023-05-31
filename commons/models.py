from django.db import models


class CommonModel(models.Model):

    """Common Model for tracking created and updated time"""

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        """This model is abstract"""

        abstract = True
