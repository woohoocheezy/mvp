from datetime import datetime, timedelta
import pyfcm
from firebase_admin import credentials, firestore
from config.settings import firebase_server_api_key
from celery import shared_task

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "my_django_project.settings")
application = get_wsgi_application()
from items.models import Item

db = firestore.client()


@shared_task
def send_push_notifications():
    """
    time_threshold = datetime.now() - timedelta(days=15)
    # time_threshold = time_threshold.date()
    print(time_threshold)
    # print(time_threshold.date())
    chats_ref = db.collection("chat")
    chats = chats_ref.where("createDate", "==", time_threshold).stream()
    # chats = chats_ref.stream()
    """

    time_threshold = datetime.now() - timedelta(days=16)
    next_day = time_threshold + timedelta(days=1)

    # print(datetime.now())
    # print(time_threshold)
    # print(next_day)

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
        # print(chat_data["createDate"])  # need to remove

        from django.utils import timezone

        utc_createDate = chat_data["createDate"].replace(tzinfo=timezone.utc)
        local_createDate = timezone.localtime(utc_createDate)
        print(local_createDate)

        # print(chat_data)  # need to remove

        # count += 1# need to remove

        # """
        # # need to remove
        # if "userId" not in chat_data.keys():
        #     continue
        # """

        userID = chat_data["userId"][0]
        # # userID = chat_data["userId"][1]  # need to remove

        # """
        # # need to remove
        # if userID != "D439KIogxNfyaUOvmklBnw8ysJX2":
        #     continue
        # """

        # """

        # message_title = "Check your deal"
        # message_body = "If you have made a deal, please click the button to confirm the transaction."

        # push_service = pyfcm.FCMNotification(
        #     api_key=firebase_server_api_key,
        # )

        # user_ref = db.collection("user").document(userID)
        # user = user_ref.get().to_dict()

        # result = push_service.notify_single_device(
        #     registration_id=user[
        #         "fcmToken"
        #     ],  # This field might be different, as you need to store the FCM Token for each user
        #     message_title=message_title,
        #     message_body=message_body,
        #     # extra_notification_kwargs={
        #     #     "icon": "https://imagedelivery.net/KS5WPV3zTnZqfcRPYRlsow/1f01c094-d581-4d30-c64b-9a2e440dbb00/public"
        #     # },
        # )

        # print(result)

        # count += 1

        # if count != 0:
        #     break
        # """

        productID = chat_data["productId"]
        # # print(productID)

        print(userID, productID)

        try:
            # print(userID, "yes")
            item = Item.objects.get(pk=productID)

        except Item.DoesNotExist:
            # print(userID, "no")
            continue

        # print(Item.objects.get(pk=productID).is_sold)
        if item.is_sold == False:
            user_ref = db.collection("user").document(userID)
            user = user_ref.get().to_dict()

            # print(user)

            # push_service = pyfcm.FCMNotification(
            #     api_key=firebase_server_api_key,
            # )

            # user_ref = db.collection("user").document(userID)
            # user = user_ref.get().to_dict()
            # print(user)

            if user["chatNotificationAllowed"]:
                push_service = pyfcm.FCMNotification(
                    api_key=firebase_server_api_key,
                )
                # message_title = "거래가 완료되었나요?"
                # message_body = "거래가 완료되었다면 업로드 하신 판매글의 '판매완료 처리'버튼을 눌러주세요. 터치 한번으로 저희 서비스 기능 향상에 큰 도움이 돼요:) 감사합니다."

                # if user["nickName"] != "니가무라":
                #     continue

                # print(userID, "sent")

                result = push_service.notify_single_device(
                    registration_id=user[
                        "fcmToken"
                    ],  # This field might be different, as you need to store the FCM Token for each user
                    message_title=message_title,
                    message_body=message_body,
                )
