from django.urls import path
from .views import (
    UserFixedPriceItemSellingList,
    UserAuctionItemSellingList,
    UserSoldList,
    BusinessLicense,
    UserFixedPriceItemPurchaseList,
    UserAuctionItemPurchaseList,
)

urlpatterns = [
    path("solds", UserSoldList.as_view()),
    path("sells/auction", UserAuctionItemSellingList.as_view()),
    path("sells/fixed-price", UserFixedPriceItemSellingList.as_view()),
    path("business-license", BusinessLicense.as_view()),
    path("purchases/fixed-price", UserFixedPriceItemPurchaseList.as_view()),
    path("purchases/auction", UserAuctionItemPurchaseList.as_view()),
]
