from django.urls import path
from .views import (
    FixedPriceItemWishlistDetail,
    AuctionItemWishlistDetail,
    FixedPriceItemWishlistToggle,
    AuctionItemWishlistToggle,
)

urlpatterns = [
    path("fixed-price", FixedPriceItemWishlistDetail.as_view()),
    path("auction", AuctionItemWishlistDetail.as_view()),
    path(
        "fixed-price/items/<str:item_pk>",
        FixedPriceItemWishlistToggle.as_view(),
    ),
    path(
        "auction/items/<str:item_pk>",
        AuctionItemWishlistToggle.as_view(),
    ),
]
