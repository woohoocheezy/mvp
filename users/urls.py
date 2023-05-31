from django.urls import path
from .views import UserSellingList, UserSoldList, BusinessLicense

urlpatterns = [
    path("sells", UserSellingList.as_view()),
    path("solds", UserSoldList.as_view()),
    path("business-license", BusinessLicense.as_view())
    # path("<int:pk>"),
    # path("<int:pk>/business-license"),
]
