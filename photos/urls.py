from django.urls import path
from .views import Photos, GetUploadURL

urlpatterns = [
    path("get-url", GetUploadURL.as_view()),
]
