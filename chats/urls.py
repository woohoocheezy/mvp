from django.urls import path
from .views import FixedPriceChat, ChatList


urlpatterns = [
    path("user", ChatList.as_view()),
    path("new", FixedPriceChat.as_view()),
]
