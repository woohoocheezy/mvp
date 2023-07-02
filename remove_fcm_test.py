from pyfcm import FCMNotification
from config.settings import firebase_credentials_json


def send_push_notification(tokens, title, message):
    push_service = FCMNotification(api_key=firebase_credentials_json)
    result = push_service.notify_single_device(
        registration_id=tokens,
        message_title=title,
        message_body=message,
    )

    return result


# print(firebase_credentials_json)
