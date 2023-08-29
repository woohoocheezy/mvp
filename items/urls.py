from django.urls import path
from .views import (
    FixedPriceItemDetail,
    FixedPriceItems,
    FixedPriceItemPurchase,
    FixedPriceItemDelete,
)

# ItemPhotos

urlpatterns = [
    path("fixed-price/", FixedPriceItems.as_view()),
    path("fixed-price/<str:pk>", FixedPriceItemDetail.as_view()),
    path("fixed-price/<str:pk>/is_sold", FixedPriceItemPurchase.as_view()),
    path("fixed-price/<str:pk>/is_deleted", FixedPriceItemDelete.as_view()),
    path("auction/", FixedPriceItems.as_view()),
    path("auction/<str:pk>", FixedPriceItemDetail.as_view()),
    path("auction/<str:pk>/is_sold", FixedPriceItemPurchase.as_view()),
    path("auction/<str:pk>/is_deleted", FixedPriceItemDelete.as_view()),
]
