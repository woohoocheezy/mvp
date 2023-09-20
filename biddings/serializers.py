from rest_framework.serializers import (
    ModelSerializer,
    CharField,
    PrimaryKeyRelatedField,
)
from .models import Bidding
from items.models import AuctionItem


class BiddingSerializer(ModelSerializer):
    auction_item = PrimaryKeyRelatedField(queryset=AuctionItem.objects.all())

    class Meta:
        model = Bidding

        fields = ["bidding_uuid", "user", "bidding_price", "auction_item"]
        read_only_fields = ["bidding_uuid"]
