from rest_framework.exceptions import NotFound
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Chat
from .serializers import ChatCreateSerializer, ChatListSerializer
from items.models import FixedPriceItem
from users.models import CustomUser


class FixedPriceChat(APIView):
    def post(self, request):
        # user = request.user

        # item_uuid = request.data["item_uuid"]
        # item = FixedPriceItem.objects.get(item_uuid=item_uuid)

        # seller_id = request.data["user_id"]
        # seller = CustomUser.objects.get(user_uuid=seller_id)

        # print(user, item, seller)

        # chat, created = ChatSerializer(seller=seller, buyer=user, item=item)

        # print(chat, created)
        data = request.data.copy()
        data["buyer"] = request.user.user_uuid
        data["seller"] = data.pop("user_id")

        print(data, request.data)

        serializer = ChatCreateSerializer(data=data, context={"request": request})

        if serializer.is_valid():
            chat = serializer.save()
            print(chat.chat_uuid)
            return Response({"chat_uuid": str(chat.chat_uuid)})

        return Response(serializer.errors, status=400)


class ChatList(APIView):
    def get_chats(self, user):
        try:
            return Chat.objects.filter(seller=user) | Chat.objects.filter(buyer=user)
        except Chat.DoesNotExist:
            raise NotFound

    def get(self, request):
        user = request.user

        chats = self.get_chats(user)

        serializer = ChatListSerializer(chats, many=True)
        print(serializer.data)

        return Response(serializer.data)


# class ChatDetail(APIView):

#     def get(self, request, uuid):

#         uuid =
