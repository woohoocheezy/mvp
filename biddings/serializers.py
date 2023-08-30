from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    PrimaryKeyRelatedField,
)
from .models import Bidding
from items.models import AuctionItem


class BiddingSerializer(ModelSerializer):
    user_id = CharField()
    auction_item = PrimaryKeyRelatedField(queryset=AuctionItem.objects.all())

    class Meta:
        model = Bidding

        fields = ["bidding_uuid", "user_id", "bidding_price", "auction_item"]
        read_only_fields = ["bidding_uuid"]
