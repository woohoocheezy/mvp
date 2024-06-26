from django.urls import path
from .views import (
    EnterChat,
    ChatList,
    ChatDetail,
    LeaveChatRoom,
    BuyerList,
    MessageIsRead,
)


urlpatterns = [
    path("user", ChatList.as_view()),
    path("enter", EnterChat.as_view()),
    path("<uuid:pk>", ChatDetail.as_view()),
    path("<uuid:pk>/leave", LeaveChatRoom.as_view()),
    path("<uuid:item_uuid>/buyer", BuyerList.as_view()),
    path("<uuid:message_uuid>/is_read", MessageIsRead.as_view()),
]
