from datetime import datetime, timedelta
import pyfcm
from firebase_admin import credentials, firestore
from config.settings import firebase_server_api_key
from celery import shared_task

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
application = get_wsgi_application()
from items.models import Item

db = firestore.client()


@shared_task
def send_push_notifications():
    time_threshold = datetime.now() - timedelta(days=16)
    next_day = time_threshold + timedelta(days=1)

    chats_ref = db.collection("chat")
    chats = (
        chats_ref.where("createDate", ">=", time_threshold)
        .where("createDate", "<", next_day)
        .stream()
    )

    message_title = "거래가 완료되었나요?"
    message_body = "거래가 완료되었다면 업로드 하신 판매글의 '판매완료 처리'버튼을 눌러주세요. 터치 한번으로 저희 서비스 기능 향상에 큰 도움이 돼요:) 감사합니다."

    for chat in chats:
        chat_data = chat.to_dict()

        from django.utils import timezone

        userID = chat_data["userId"][0]

        productID = chat_data["productId"]

        try:
            item = Item.objects.get(pk=productID)

        except Item.DoesNotExist:
            continue

        if item.is_sold == False:
            user_ref = db.collection("user").document(userID)
            user = user_ref.get().to_dict()

            if user["chatNotificationAllowed"]:
                push_service = pyfcm.FCMNotification(
                    api_key=firebase_server_api_key,
                )

                result = push_service.notify_single_device(
                    registration_id=user["fcmToken"],
                    message_title=message_title,
                    message_body=message_body,
                )
