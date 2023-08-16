from django.contrib.auth.backends import BaseBackend
from users.models import CustomUser
from django.contrib.auth.models import User


class CustomUserAuthenticationBackend(BaseBackend):

    """Custom User Authntication"""

    def authenticate(self, request, phone_number=None, **kwargs):
        try:
            custom_user = CustomUser.objects.get(phone_number=phone_number)
            return custom_user.user
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
