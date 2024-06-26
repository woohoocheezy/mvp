from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from chats import consumers

websocket_urlpatterns = [
    path("ws/chat/<uuid:chat_uuid>", consumers.ChatConsumer.as_asgi()),
]

application = ProtocolTypeRouter(
    {
        "websocket": URLRouter(websocket_urlpatterns),
    }
)
