from django.urls import path
from .views import (
    FixedPriceItemDetail,
    FixedPriceItems,
    FixedPriceItemPurchase,
    FixedPriceItemDelete,
    AuctionItemDetail,
    AuctionItems,
    AuctionItemPurchase,
    AuctionItemDelete,
)

# ItemPhotos

urlpatterns = [
    path("fixed-price", FixedPriceItems.as_view()),
    path("fixed-price/<str:pk>", FixedPriceItemDetail.as_view()),
    path("fixed-price/<str:pk>/is_sold", FixedPriceItemPurchase.as_view()),
    path("fixed-price/<str:pk>/is_deleted", FixedPriceItemDelete.as_view()),
    path("auction", AuctionItems.as_view()),
    path("auction/<str:pk>", AuctionItemDetail.as_view()),
    path("auction/<str:pk>/is_sold", AuctionItemPurchase.as_view()),
    path("auction/<str:pk>/is_deleted", AuctionItemDelete.as_view()),
]
