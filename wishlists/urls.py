from django.urls import path
from .views import WishlistDetail, WishlistToggle

urlpatterns = [
    path("", WishlistDetail.as_view()),
    path("items/<int:item_pk>", WishlistToggle.as_view()),
]
