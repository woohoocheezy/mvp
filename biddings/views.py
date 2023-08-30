from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, NotFound
from rest_framework.response import Response
from items.models import AuctionItem
from .models import Bidding
from .serializers import BiddingSerializer


class MakeBidding(APIView):
    def get_auction_item(self, item_pk):
        try:
            return AuctionItem.objects.get(pk=item_pk)

        except AuctionItem.DoesNotExist:
            raise NotFound

    def post(self, request, item_pk):
        user_id = request.user.get("uid")
        auction_item = self.get_auction_item(item_pk)

        if Bidding.objects.filter(user_id=user_id, auction_item__pk=item_pk).exists():
            raise ValidationError("이미 해당 상품에 대해 입찰함")

        if request.data["bidding_price"] < auction_item.lowest_price:
            raise ValidationError("최저가보다 낮은 입찰가임")

        data = request.data
        data["user_id"] = user_id
        data["auction_item"] = item_pk

        # print(data["auction_item"])

        serializer = BiddingSerializer(data=data)

        if serializer.is_valid():
            bidding = serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(password)
#             user.save()

#             serializer = PrivateUserSerializer(user)

#             return Response(serializer.data)

#         else:
#             return Response(serializer.errors)
