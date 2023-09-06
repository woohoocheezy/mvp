try:
    import os
    import sys
    from django import setup

    # Add project root directory to sys.path
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
    sys.path.insert(0, PROJECT_ROOT)

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    setup()

    from datetime import date, timedelta, datetime
    from items.models import AuctionItem
    from firebase_admin import firestore

    def send_msg_auction_deadline():
        """create messages to items which the deadline is over today.

        Keyword arguments:
        Return: Nothing
        """

        yesterday = date.today() - timedelta(days=1)

        auction_items = AuctionItem.objects.filter(deadline=yesterday, is_overdue=True)

        # print(len(auction_items))
        # db = firestore.client()

        for item in auction_items:
            if item.is_bidded:
                item.is_sold = True

                highest_bidding = item.biddings.order_by(
                    "-bidding_price", "created_at"
                ).first()
                item.winning_bid = highest_bidding.bidding_price
                item.buy_user_id = highest_bidding.user_id
                print("highest bidding matched msg sent")

                # print(item, item.user_id)
                # print(
                #     highest_bidding,
                #     highest_bidding.user_id,
                # )


                # create a chat room on firestore database
                # doc_ref = db.collection("chat").document()

                # # set data for the chat room document
                # doc_ref.set(
                #     {
                #         "createDate": firestore.SERVER_TIMESTAMP,
                #         "enteredUserId": [item.user_id, highest_bidding.user_id],
                #         "lastChat": "경매가 완료되어, 판매자분과 최고 입찰자분이 매칭되었어요!",
                #         "lastChatDate": firestore.SERVER_TIMESTAMP,
                #         "productId": str(item.item_uuid),
                #         "title": item.item_name,
                #         "userId": [item.user_id, highest_bidding.user_id],
                #     }
                # )

            else:
                # official_account_id = "YfeceAVnL1MKWyd1TjBWYkRHi3l1"

                # user_ref = db.collection("user").document(item.user_id)
                # user = user_ref.get().to_dict()
                # print(item.user_id, user)

                # # create a chat room on firestore database
                # doc_ref = db.collection("chat").document()

                # set data for the chat room document
                # doc_ref.set(
                #     {
                #         "createDate": firestore.SERVER_TIMESTAMP,
                #         "enteredUserId": [item.user_id, official_account_id],
                #         "lastChat": "경매가 완료되었지만, 입찰자가 없어요!",
                #         "lastChatDate": firestore.SERVER_TIMESTAMP,
                #         "productId": str(item.item_uuid),
                #         "title": item.item_name,
                #         "userId": [item.user_id, official_account_id],
                #     }
                )

                # create a message on Firestore database
                # msg_ref = (
                #     db.collection("chat")
                #     .document(doc_ref.id)
                #     .collection("message")
                #     .document()
                # )

                print("no bidding msg sent")

                # set data for the message document
                # msg_ref.set(
                #     {
                #         "isRead": False,
                #         "receiverId": item.user_id,
                #         "receiverToken": user["fcmToken"],
                #         "text": "",
                #         "time": firestore.SERVER_TIMESTAMP,
                #         "type": "auctionNotSell",
                #         "url": "",
                #         "userId": official_account_id,
                #     }
                # )

                # print("sad")

    if __name__ == "__main__":
        print(f"[{datetime.now()}] tasks start.")
        send_msg_auction_deadline()
        print(f"[{datetime.now()}] tasks finish.")

except Exception as e:
    print(e)
    print(f"[{datetime.now()}] tasks doesn't finish.")
