from django.urls import path
from .views import UserSellingList, UserSoldList, BusinessLicense, UserPurchaseList

urlpatterns = [
    path("sells/fixed-price", UserSellingList.as_view()),
    path("solds", UserSoldList.as_view()),
    path("business-license", BusinessLicense.as_view()),
    path("purchases/fixed-price", UserPurchaseList.as_view()),
]
