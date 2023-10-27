from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer
from json import loads, dumps
from pyfcm import FCMNotification
from config.settings import firebase_server_api_key

import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.chat_uuid = self.scope["url_route"]["kwargs"]["chat_uuid"]
        self.room_group_name = "chat_%s" % self.chat_uuid
        self.chat = await self.get_chat()

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )

    # Recieve message from WebSocket
    async def receive(self, text_data):
        text_data_json = loads(text_data)
        message = text_data_json["message"]
        type = text_data_json["type"]
        user_id = text_data_json["user_id"]

        # Save message on the database
        # Get User instances for sender and reciever
        sender_user, reciever_user = await self.get_users(user_id)

        # Create and Store the message on DB
        try:
            await self.create_message(type, sender_user, reciever_user, message)

            # Send message to room group
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "sender_id": user_id,
                    "content_type": type,
                },
            )
        except ValueError as e:
            if str(e) == "The receiver has left the chat room":
                logger.error(f"Failed to send a message: {e}")

                await self.send(
                    text_data=dumps({"error": f"Failed to send message: {e}"})
                )
            else:
                raise e

    # Recieve message from room group
    async def chat_message(self, event):
        message = event["message"]
        sender_id = event["sender_id"]
        content_type = event["content_type"]

        # Send message to WebSocket
        await self.send(
            text_data=dumps(
                {
                    "content_type": content_type,
                    "message": message,
                    "sender_id": sender_id,
                }
            )
        )

    @database_sync_to_async
    def get_users(self, user_id):
        if str(self.chat.seller.user_uuid) == user_id:
            return self.chat.seller, self.chat.buyer
        elif str(self.chat.buyer.user_uuid) == user_id:
            return self.chat.buyer, self.chat.seller
        else:
            raise ValueError("Wrong User")

    @database_sync_to_async
    def get_chat(self):
        from .models import Chat

        return Chat.objects.get(chat_uuid=self.chat_uuid)

    @database_sync_to_async
    def create_message(self, type, sender_user, receiver_user, message):
        from .models import Message

        self.chat.refresh_from_db()

        # Check if the receiver is still in the chat room
        if (receiver_user == self.chat.seller and not self.chat.seller_active) or (
            receiver_user == self.chat.buyer and not self.chat.buyer_active
        ):
            raise ValueError("The receiver has left the chat room")

        logger.info(f"{self.chat.seller_active} & {self.chat.buyer_active}")

        push_service = FCMNotification(
            api_key=firebase_server_api_key,
        )

        if type == "text":
            message = Message.objects.create(
                text=message,
                type=type,
                sender_user_id=sender_user,
                receiver_user_id=receiver_user,
                chat=self.chat,
            )

            result = push_service.notify_single_device(
                registration_id=message.receiver_user_id.fcm_token,
                message_title=message.sender_user_id.nick_name,
                message_body=message.text,
            )
        elif type == "image":
            message = Message.objects.create(
                image=message,
                type=type,
                sender_user_id=sender_user,
                receiver_user_id=receiver_user,
                chat=self.chat,
            )

            result = push_service.notify_single_device(
                registration_id=message.receiver_user_id.fcm_token,
                message_title=message.sender_user_id.nick_name,
                message_body="이미지",
            )

        else:
            raise ValueError("Wrong type of message")

        return message
