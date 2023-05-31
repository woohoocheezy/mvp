import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class User(AbstractBaseUser):
    """User Model"""

    username = models.CharField(max_length=20)  # nickname
    # uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    # name = models.CharField(default="", max_length=20)  # real name of user

    # phone_number = models.IntegerField(blank=False, null=False)

    # """사업자등록증 관련 정보"""
    # # if the user certificate own business license reegistration(사업자등록증)
    # is_business_license_certificated = models.BooleanField(default=False)
    # license_number = models.IntegerField()
    # license_name = models.CharField(max_length=20)
    # license_date = models.DateField()

    # """지역 관련 정보"""
    # # if the user is certificate own local area
    # is_local_certificated = models.BooleanField(default=False)
