import datetime
import string
import random
import secrets
from django.contrib.auth.models import User
from firebase_admin import firestore
from users.models import CustomUser
from items.models import FixedPriceItem, AuctionItem
from wishlists.models import Wishlist


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


def change_unknown_data():
    temp = FixedPriceItem.objects.filter(user_id="YffrXPieCvgV2cQAn2HPkFTyhMJ3")
    print(len(temp))
    temp.update(user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = FixedPriceItem.objects.filter(user_id="D439KIogxNfyaUOvmklBnw8ysJX2")
    print(len(temp))
    temp.update(user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = FixedPriceItem.objects.filter(buy_user_id="YffrXPieCvgV2cQAn2HPkFTyhMJ3")
    print(len(temp))
    temp.update(buy_user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = FixedPriceItem.objects.filter(buy_user_id="D439KIogxNfyaUOvmklBnw8ysJX2")
    print(len(temp))
    temp.update(buy_user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = AuctionItem.objects.filter(user_id="YffrXPieCvgV2cQAn2HPkFTyhMJ3")
    print(len(temp))
    temp.update(user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = AuctionItem.objects.filter(user_id="D439KIogxNfyaUOvmklBnw8ysJX2")
    print(len(temp))
    temp.update(user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = AuctionItem.objects.filter(buy_user_id="YffrXPieCvgV2cQAn2HPkFTyhMJ3")
    print(len(temp))
    temp.update(buy_user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = AuctionItem.objects.filter(buy_user_id="D439KIogxNfyaUOvmklBnw8ysJX2")
    print(len(temp))
    temp.update(buy_user_id="0EAimXI713deuRi3h3rIgiFvCyx1")

    temp = AuctionItem.objects.filter(buy_user_id="KO6ZdGoXkmQAI3dEfcjV8WSbLeI2")
    print(len(temp))
    temp.update(buy_user_id="0EAimXI713deuRi3h3rIgiFvCyx1")


def migrate_user_data():
    db = firestore.client()

    users_ref = db.collection("user")
    users = users_ref.get()

    # count = 0

    for user in users:
        data = user.to_dict()

        if CustomUser.objects.filter(phone_number=data["phoneNumber"]).exists():
            continue

        # keys = data.keys()
        # print(f"No.[{count}]", data["userId"])
        # count += 1

        # if "name" not in data.keys():
        #     print(len(keys), "no name field from data")
        #     for key in keys:
        #         print(key, end=" ")
        #     print()
        #     print()
        #     continue

        # print(len(keys), f"{data['name']}")
        # for key in keys:
        #     print(key, end=" ")
        # print()
        # print()

        if "name" not in data.keys():
            data["name"] = ""

        if data["name"] is None:
            data["name"] = ""

        if (
            "birthDate" not in data.keys()
            or data["birthDate"] is None
            or data["birthDate"] == ""
            or len(data["birthDate"]) != 8
        ):
            data["birthDate"] = datetime.date(1900, 1, 1)

        if "sector" not in data.keys() or data["sector"] is None:
            data["sector"] = "test"

        if data["phoneNumber"] is None:
            data["phoneNumber"] = "000-0000-0000"

        if data["userType"] is None or data["userType"] == "own":
            data["userType"] = "local"

        if len(data["nickName"]) > 10:
            data["nickName"] = data["nickName"][:10]

        if "kakaoId" not in data.keys():
            data["kakaoId"] = None

        print(data["userId"])

        auth_user = create_random_user()

        if data["userType"] == "apple":
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
                apple_id=data["kakaoId"],
                temp_user_id=data[
                    "userId"
                ],  # this is for saving firebase uid cause it's needed when migrating the buy_user
            )
        else:
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
                temp_user_id=data[
                    "userId"
                ],  # this is for saving firebase uid cause it's needed when migrating the buy_user
            )

        user_obj.save()

        fixed_items = FixedPriceItem.objects.filter(user_id=data["userId"])

        if fixed_items.exists():
            fixed_items.update(temp_user=user_obj.user_uuid)
            print(f"fixed done")

        auction_items = AuctionItem.objects.filter(user_id=data["userId"])

        if auction_items.exists():
            auction_items.update(temp_user=user_obj.user_uuid)
            print(f"auction done")


def migrate_the_buy_user():
    fixed_items = FixedPriceItem.objects.filter(is_sold=True)

    for fixed_item in fixed_items:
        print(fixed_item, fixed_item.buy_user_id)
        if CustomUser.objects.filter(temp_user_id=fixed_item.buy_user_id).exists():
            fixed_item.temp_buy_user = CustomUser.objects.get(
                temp_user_id=fixed_item.buy_user_id
            )
            fixed_item.save()
        else:
            print("fuck3")
            # fixed_item.is_sold = False
            # fixed_item.save()

    auction_items = AuctionItem.objects.filter(is_sold=True)

    for auction_item in auction_items:
        print(auction_item, auction_item.buy_user_id)
        if CustomUser.objects.filter(temp_user_id=auction_item.buy_user_id).exists():
            auction_item.temp_buy_user = CustomUser.objects.get(
                temp_user_id=auction_item.buy_user_id
            )
            auction_item.save()
        else:
            print("fuck2")
            auction_item.temp_buy_user = CustomUser.objects.get(nick_name="트레져")
            auction_item.save()


def migrate_bid_data():
    from biddings.models import Bidding

    biddings = Bidding.objects.all()

    for bid in biddings:
        if CustomUser.objects.filter(temp_user_id=bid.user_id).exists():
            bid.temp_user = CustomUser.objects.get(temp_user_id=bid.user_id)
            bid.save()
        else:
            print("fuck1")
            bid.temp_user = CustomUser.objects.get(nick_name="트레져")
            bid.save()


def migrate_wishlist_data():
    wishlists = Wishlist.objects.all()

    for wishlist in wishlists:
        if CustomUser.objects.filter(temp_user_id=wishlist.user_id).exists():
            wishlist.temp_user = CustomUser.objects.get(temp_user_id=wishlist.user_id)
            wishlist.save()

        else:
            wishlist.delete()
