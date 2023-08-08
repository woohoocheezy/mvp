from django.db import models
from django.conf import settings
import uuid


class CustomUser(models.Model):

    """User model for 소상공간"""

    class UserTypeChoices(models.TextChoices):
        KAKAO = ("kakao", "Kakao Login")
        APPLE = ("apple", "Apple Login")
        LOCAL = ("local", "Local Login")

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="custom_user"
    )

    username = None
    password = None

    user_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    chat_notification_allowed = models.BooleanField(default=True)
    marketing_notification_allowed = models.BooleanField(default=True)
    is_certificated = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    fcm_token = models.TextField(null=True, blank=True)
    nick_name = models.CharField(max_length=10)
    name = models.CharField(max_length=13)
    birth_date = models.DateField()
    sector = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=11, unique=True)
    profile_image_url = models.URLField(null=True, blank=True)
    user_type = models.CharField(
        max_length=10,
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.LOCAL,
    )
    kakao_id = models.CharField(max_length=100, null=True, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        blank=True,
        related_query_name="customuser",
        related_name="customuser_set",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        blank=True,
        related_query_name="customuser",
        related_name="customuser_set",
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nick_name
