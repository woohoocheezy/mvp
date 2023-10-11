from django.urls import path
from .views import EnterChat, ChatList, ChatDetail, LeaveChatRoom


urlpatterns = [
    path("user", ChatList.as_view()),
    path("enter", EnterChat.as_view()),
    path("<uuid:pk>", ChatDetail.as_view()),
    path("<uuid:pk>/leave", LeaveChatRoom.as_view()),
]
