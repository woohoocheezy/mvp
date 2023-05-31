from django.urls import path
from .views import Wishlists, WishlistDetail, WishlistToogle

urlpatterns = [
    path("", WishlistDetail.as_view()),
    path("items/<int:item_pk>", WishlistToogle.as_view()),
]
