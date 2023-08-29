from django.urls import path
from .views import Wishlists, WishlistDetail, WishlistToggle

urlpatterns = [
    path("fixed-price/", WishlistDetail.as_view()),
    path("items/fixed-price/<str:item_pk>", WishlistToggle.as_view()),
]
