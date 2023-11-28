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
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="custom_user",
        null=True,
    )

    username = None
    password = None

    user_uuid = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False, unique=True
    )
    chat_notification_allowed = models.BooleanField(
        default=True
    )  # push_notification_allowed로 이름 변경 고민해볼 것
    marketing_notification_allowed = models.BooleanField(default=True)
    is_certificated = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    fcm_token = models.TextField(null=True, blank=True)  # null, blank 삭제 필요
    nick_name = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=13)
    birth_date = models.DateField(null=True, blank=True)
    sector = models.CharField(max_length=13)
    phone_number = models.CharField(max_length=60, unique=True)
    profile_image_url = models.URLField(null=True, blank=True)
    user_type = models.CharField(
        max_length=10,
        choices=UserTypeChoices.choices,
        default=UserTypeChoices.LOCAL,
    )
    kakao_id = models.CharField(max_length=100, null=True, blank=True)
    apple_id = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(max_length=15, null=True, blank=True)

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

    blocked_users = models.ManyToManyField("self", symmetrical=True, blank=True)

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.nick_name

    @property
    def is_authenticated(self):
        return self.user.is_authenticated
