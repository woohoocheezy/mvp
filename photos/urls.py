from django.urls import path
from .views import Photos, GetUploadURL, GetCFUploadURL

urlpatterns = [
    path("get-url", GetUploadURL.as_view()),
    path("get-cfurl", GetCFUploadURL.as_view()),
]
