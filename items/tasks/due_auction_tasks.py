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

    def check_auction_deadline():
        """check the deadline of each auction items and change the 'is_overdue' status if it's over on every 12:03 pm

        Keyword arguments:
        Return: Nothing
        """

        yesterday = date.today() - timedelta(days=1)

        overdue_auction_items = AuctionItem.objects.filter(
            deadline=yesterday, is_deleted=False
        )

        # print(len(overdue_auction_items))

        for item in overdue_auction_items:
            item.is_overdue = True
            item.save()

            print(item, item.biddings.all())

            if item.biddings.exists():
                # print(item, "hi")
                item.is_bidded = True
                item.save()

                # highest_bidding = item.biddings.order_by("-bidding_price").first()
                # print(highest_bidding)

    if __name__ == "__main__":
        print(f"[{datetime.now()}] tasks start.")
        check_auction_deadline()
        print(f"[{datetime.now()}] tasks finish.")

except Exception as e:
    print(e)
    print(f"[{datetime.now()}] tasks doesn't finish.")
