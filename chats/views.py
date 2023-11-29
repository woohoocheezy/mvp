from django.db.models import Max
from django.db.models.functions import Coalesce
from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from config.settings import PAGE_SIZE
from items.models import FixedPriceItem
from .models import Chat, Message
from .serializers import ChatDetailSerializer, ChatListSerializer, MessageSerializer


import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EnterChat(APIView):
    def post(self, request):
        data = request.data.copy()
        data["buyer"] = request.user.user_uuid
        data["seller"] = data.pop("user_id")

        # print(data, request.data)

        serializer = ChatDetailSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            try:
                existing_chat = Chat.objects.get(
                    seller=data["seller"],
                    buyer=data["buyer"],
                    object_id=data["item_uuid"],
                )
                existing_chat.buyer_active = True
                existing_chat.save()
                return Response({"chat_uuid": str(existing_chat.chat_uuid)})
            except Chat.DoesNotExist:
                chat = serializer.save()
                # print(chat.chat_uuid)
                return Response({"chat_uuid": str(chat.chat_uuid)})

        return Response(serializer.errors, status=400)


class ChatList(APIView):
    def get_chats(self, user):
        try:
            blocked_user_ids = user.blocked_users.all().values_list(
                "user_uuid", flat=True
            )
            chats = Chat.objects.filter(seller=user, seller_active=True).exclude(
                buyer__in=blocked_user_ids
            ) | Chat.objects.filter(buyer=user, buyer_active=True).exclude(
                seller__in=blocked_user_ids
            )
            chats = chats.annotate(
                last_chat_date=Coalesce(Max("messages__time_sent"), "created_at")
            ).order_by("-last_chat_date")
            return chats
        except Chat.DoesNotExist:
            raise NotFound

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        user = request.user

        chats = self.get_chats(user)[start:end]

        serializer = ChatListSerializer(
            chats,
            many=True,
            context={"request": request},
        )
        print(serializer.data)

        return Response(serializer.data)


class ChatDetail(APIView):
    def get(self, request, pk):
        chat = Chat.objects.get(chat_uuid=pk)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        messages = chat.messages.order_by("-time_sent")[start:end]

        unread_messages = chat.messages.filter(
            receiver_user_id=request.user, is_read=False
        )

        for unread_message in unread_messages:
            unread_message.is_read = True
            unread_message.save()

        serializer = MessageSerializer(messages, many=True)

        return Response(serializer.data)


class LeaveChatRoom(APIView):
    def get_chat(self, pk):
        try:
            return Chat.objects.get(chat_uuid=pk)
        except Chat.DoesNotExist:
            raise NotFound

    def post(self, request, pk):
        user = request.user
        chat = self.get_chat(pk)

        if chat.seller == user:
            chat.seller_active = False

        elif chat.buyer == user:
            chat.buyer_active = False
        else:
            return Response({"error": "Invalid user"}, status=400)

        chat.save()

        if not (chat.buyer_active or chat.seller_active):
            Message.objects.filter(chat=chat).delete()
            Chat.objects.filter(chat_uuid=chat.chat_uuid).delete()

        return Response(status=HTTP_200_OK)


class BuyerList(APIView):
    def get_chats(self, request_user, item_uuid):
        try:
            chats = Chat.objects.filter(seller=request_user, object_id=item_uuid)
            chats = chats.annotate(
                last_chat_date=Coalesce(Max("messages__time_sent"), "created_at")
            ).order_by("-last_chat_date")
            return chats
        except Chat.DoesNotExist:
            raise NotFound

    def get(self, request, item_uuid):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        request_user = request.user

        chats = self.get_chats(request_user, item_uuid)[start:end]

        serializer = ChatListSerializer(
            chats,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class MessageIsRead(APIView):
    def put(self, request, message_uuid):
        try:
            message = Message.objects.get(message_uuid=message_uuid)
            message.is_read = True
            message.save()
        except Message.DoesNotExist:
            raise NotFound

        return Response(HTTP_200_OK)
