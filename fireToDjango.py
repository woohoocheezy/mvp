import datetime
import string
import random
import secrets
from django.contrib.auth.models import User
from firebase_admin import firestore
from users.models import CustomUser


def random_string_generator(length=10):
    letters = string.ascii_letters
    return "".join(secrets.choice(letters) for _ in range(length))


def random_email_generator(length=5, domain="example.com"):
    random_prefix = random_string_generator(length)
    return f"{random_prefix}@{domain}"


def create_random_user():
    username = random_string_generator()
    email = random_email_generator()
    password = "".join(
        random.choices(
            string.ascii_uppercase + string.ascii_lowercase + string.digits, k=10
        )
    )
    auth_user = User.objects.create_user(username, email, password)
    return auth_user


def migrate_data():
    db = firestore.client()

    users_ref = db.collection("user")
    users = users_ref.get()

    count = 0

    for user in users:
        data = user.to_dict()

        if "name" not in data.keys():
            continue

        # if data["name"] != "이용원", "":
        #     continue
        print(data["name"])

        if data["name"] is None:
            data["name"] = ""

        if data["birthDate"] is None:
            data["birthDate"] = datetime.date(1900, 1, 1)

        if data["sector"] is None:
            data["sector"] = "test"

        if data["phoneNumber"] is None:
            data["phoneNumber"] = "000-0000-0000"

        if data["userType"] is None:
            data["userType"] = "local"

        auth_user = create_random_user()

        user_obj = CustomUser.objects.create(
            user=auth_user,
            chat_notification_allowed=data["chatNotificationAllowed"],
            marketing_notification_allowed=data["marketingNotificationAllowed"],
            is_certificated=data["isCertificated"],
            create_at=data["createDate"].strftime("%Y-%m-%dT%H:%M:%SZ"),
            fcm_token=data["fcmToken"],
            nick_name=data["nickName"],
            name=data["name"],
            birth_date=data["birthDate"],
            sector=data["sector"],
            phone_number=data["phoneNumber"],
            profile_image_url=data["profileImageUrl"],
            user_type=data["userType"],
            kakao_id=data["kakaoId"],
        )

        user_obj.save()

        print(count)
        count += 1
