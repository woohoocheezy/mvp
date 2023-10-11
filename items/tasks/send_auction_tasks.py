try:
    import os
    import sys
    from django import setup

    # Add project root directory to sys.path
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    sys.path.insert(0, PROJECT_ROOT)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    setup()

    from django.contrib.contenttypes.models import ContentType
    from datetime import date, timedelta, datetime
    from pyfcm import FCMNotification
    from items.models import AuctionItem
    from chats.models import Chat, Message
    from users.models import CustomUser
    from config.settings import firebase_server_api_key

    def send_msg_auction_deadline():
        """create messages to items which the deadline is over today.

        Keyword arguments:
        Return: Nothing
        """

        yesterday = date.today() - timedelta(days=2)

        auction_items = AuctionItem.objects.filter(deadline=yesterday, is_overdue=True)

        for item in auction_items:
            # print(item)
            if item.is_bidded:
                item.is_sold = True

                highest_bidding = item.biddings.order_by(
                    "-bidding_price", "created_at"
                ).first()
                item.winning_bid = highest_bidding.bidding_price
                item.buy_user_id = highest_bidding.user_id
                item.save()

                # create a chat room for seller and the highest bidder
                content_type = ContentType.objects.get_for_model(item)
                chat, created = Chat.objects.get_or_create(
                    seller=item.user,
                    buyer=highest_bidding.user,
                    content_type=content_type,
                    object_id=item.item_uuid,
                    title=item.item_name,
                    defaults={
                        "seller_active": True,
                        "buyer_active": True,
                    },
                )

            else:
                official_account_user = CustomUser.objects.get(nick_name="매니저")

                # create a chat room
                content_type = ContentType.objects.get_for_model(item)

                chat, created = Chat.objects.get_or_create(
                    seller=item.user,
                    buyer=official_account_user,
                    content_type=content_type,
                    object_id=item.item_uuid,
                    title=item.item_name,
                    defaults={
                        "seller_active": True,
                        "buyer_active": True,
                    },
                )

                # create a message
                message = Message.objects.create(
                    text="",
                    sender_user_id=official_account_user,
                    receiver_user_id=item.user,
                    type="auctionNotSell",
                    is_read=False,
                    chat=chat,
                )

                push_service = FCMNotification(
                    api_key=firebase_server_api_key,
                )
                result = push_service.notify_single_device(
                    registration_id=chat.seller.fcm_token,
                    message_title="소상공간",
                    message_body=f'"{chat.title}" 상품에 대한 경매가 완료되었지만, 입찰자가 없어요',
                )

    if __name__ == "__main__":
        print(f"[{datetime.now()}] tasks start.")
        send_msg_auction_deadline()
        print(f"[{datetime.now()}] tasks finish.")

except Exception as e:
    print(e)
    print(f"[{datetime.now()}] tasks doesn't finish.")
