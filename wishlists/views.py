from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.exceptions import NotFound
from rest_framework.status import HTTP_200_OK
from .models import Wishlist
from .serializers import (
    WishlistSerializer,
    FixedPriceItemWishlistSerializer,
    AuctionItemWishlistSerializer,
)
from items.models import FixedPriceItem, AuctionItem
from config.settings import PAGE_SIZE


class Wishlists(APIView):
    """the APIView for Item Wishlist"""

    # permission_classes = [IsAuthenticated]

    def get(self, request):
        """GET /wishilists
            Displaying all 'wishlists' that a user created

        Keyword arguments:
        self --
        request --
        Return: the response with the data of wishlist serializer
        """

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_wishilists = Wishlist.objects.filter(user_id=request.user.get("uid"))[
            start:end
        ]
        serializer = WishlistSerializer(
            all_wishilists,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)

    def post(self, request):
        """POST /wishilists
           create a 'wishlist' of a user

        Keyword arguments:
        self --
        request --
        Return: the response with the data of wishlist serializer if the serializer is valid or the error
        """
        serializer = WishlistSerializer(data=request.data)

        if serializer.is_valid():
            wishlist = serializer.save(user_id=request.user.get("uid"))
            serializer = WishlistSerializer(wishlist)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FixedPriceItemWishlistDetail(APIView):
    """The API view of the detail information of 'Wishlist'
       Handling requests for 'GET/PUT/DELETE /wishlists/{ID of a wishlist}'
       ex) GET /wishlists/1

    Keyword arguments:
    None
    Return: None
    """

    # a user can only access its own wishlist
    # permission_classes = [IsAuthenticated]

    def get_object(self, request):
        """returning the object of a wishlist making a query by checking pk and user

        Keyword arguments:
        pk -- the pk of the wishlist
        user -- the user of the wishlist is same as the user who requests
        Return: the wishlist object of a request.user with the wishlist's pk, or NotFound
        """

        try:
            return Wishlist.objects.get(user_id=request.user.get("uid"))
        except Wishlist.DoesNotExist:
            serializer = WishlistSerializer(data=request.data)

            if serializer.is_valid():
                wishlist = serializer.save(user_id=request.user.get("uid"))
                serializer = WishlistSerializer(wishlist)
                return Wishlist.objects.get(user_id=request.user.get("uid"))
            else:
                return Response(serializer.errors)

    def get(self, request):
        """handling the request about 'GET /wishlists/{ID of a wishlist}'

        Keyword arguments:
        request -- the request that a user make
        pk -- the primary key or the requested wishlist
        Return: the serialized data of the wishlist with 'the pk & the user'
        """
        # try:
        #     page = int(request.query_params.get("page", 1))
        # except ValueError:
        #     page = 1

        # page_size = PAGE_SIZE
        # start = (page - 1) * page_size
        # end = start + page_size
        wishlist = self.get_object(request)
        print(wishlist.fixed_price_items, wishlist.auction_items)
        serializer = FixedPriceItemWishlistSerializer(
            wishlist, context={"request": request}
        )
        # print(serializer)

        return Response(serializer.data)


class AuctionItemWishlistDetail(APIView):
    """The API view of the detail information of 'Wishlist'
       Handling requests for 'GET/PUT/DELETE /wishlists/{ID of a wishlist}'
       ex) GET /wishlists/1

    Keyword arguments:
    None
    Return: None
    """

    # a user can only access its own wishlist
    # permission_classes = [IsAuthenticated]

    def get_object(self, request):
        """returning the object of a wishlist making a query by checking pk and user

        Keyword arguments:
        pk -- the pk of the wishlist
        user -- the user of the wishlist is same as the user who requests
        Return: the wishlist object of a request.user with the wishlist's pk, or NotFound
        """

        try:
            return Wishlist.objects.get(user_id=request.user.get("uid"))
        except Wishlist.DoesNotExist:
            serializer = WishlistSerializer(data=request.data)

            if serializer.is_valid():
                wishlist = serializer.save(user_id=request.user.get("uid"))
                serializer = WishlistSerializer(wishlist)
                return Wishlist.objects.get(user_id=request.user.get("uid"))
            else:
                return Response(serializer.errors)

    def get(self, request):
        """handling the request about 'GET /wishlists/{ID of a wishlist}'

        Keyword arguments:
        request -- the request that a user make
        pk -- the primary key or the requested wishlist
        Return: the serialized data of the wishlist with 'the pk & the user'
        """
        # try:
        #     page = int(request.query_params.get("page", 1))
        # except ValueError:
        #     page = 1

        # page_size = PAGE_SIZE
        # start = (page - 1) * page_size
        # end = start + page_size
        wishlist = self.get_object(request)
        serializer = AuctionItemWishlistSerializer(
            wishlist, context={"request": request}
        )
        # print(serializer)

        return Response(serializer.data)


class FixedPriceItemWishlistToggle(APIView):

    """The API view for adding/removing a item to/from the wishlist
       Handling requests for 'PUT /wishlists/{ID of a wishlist}/items/{ID of a item}'
       ex) PUT /wishlists/1/item/fixed-price/1

    Keyword arguments:
    None
    Return: None
    """

    # permission_classes = [IsAuthenticated]
    # pagination_class = PageNumberPagination

    def get_wishlist(self, user_id):
        """returning the object of a wishlist making a query by checking pk and user

        Keyword arguments:
        pk -- the pk of the wishlist
        user -- the user of the wishlist is same as the user who requests
        Return: the Wishlist object of a request.user with the wishlist's pk, or NotFound
        """

        try:
            return Wishlist.objects.get(user_id=user_id)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_item(self, pk):
        """returning the object of a item making a query by checking pk

        Keyword arguments:
        pk -- the pk of the item
        Return: the Item object of a item's pk, or NotFound
        """

        try:
            return FixedPriceItem.objects.get(pk=pk)
        except FixedPriceItem.DoesNotExist:
            raise NotFound

    def put(self, request, item_pk):
        """handling the request about 'PUT /wishlists/{ID of a wishlist}/items/{ID of a item}'

        Keyword arguments:
        request -- the request that a user make
        pk -- the primary key or the requested wishlist
        item_pk -- the pk of the item
        Return: the serialized data of the wishlist with 'the pk & the user' which is UPDATED
        """

        wishlist = self.get_wishlist(request.user.get("uid"))
        item = self.get_item(item_pk)

        print(wishlist.fixed_price_items)

        if wishlist.fixed_price_items.filter(item_uuid=item_pk).exists():
            wishlist.fixed_price_items.remove(item)
        else:
            wishlist.fixed_price_items.add(item)

        return Response(status=HTTP_200_OK)


class AuctionItemWishlistToggle(APIView):

    """The API view for adding/removing a item to/from the wishlist
       Handling requests for 'PUT /wishlists/{ID of a wishlist}/items/{ID of a item}'
       ex) PUT /wishlists/1/item/auction/1

    Keyword arguments:
    None
    Return: None
    """

    # permission_classes = [IsAuthenticated]
    # pagination_class = PageNumberPagination

    def get_wishlist(self, user_id):
        """returning the object of a wishlist making a query by checking pk and user

        Keyword arguments:
        pk -- the pk of the wishlist
        user -- the user of the wishlist is same as the user who requests
        Return: the Wishlist object of a request.user with the wishlist's pk, or NotFound
        """

        try:
            return Wishlist.objects.get(user_id=user_id)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get_item(self, pk):
        """returning the object of a item making a query by checking pk

        Keyword arguments:
        pk -- the pk of the item
        Return: the Item object of a item's pk, or NotFound
        """

        try:
            return AuctionItem.objects.get(pk=pk)
        except AuctionItem.DoesNotExist:
            raise NotFound

    def put(self, request, item_pk):
        """handling the request about 'PUT /wishlists/{ID of a wishlist}/items/{ID of a item}'

        Keyword arguments:
        request -- the request that a user make
        pk -- the primary key or the requested wishlist
        item_pk -- the pk of the item
        Return: the serialized data of the wishlist with 'the pk & the user' which is UPDATED
        """

        wishlist = self.get_wishlist(request.user.get("uid"))
        item = self.get_item(item_pk)

        if wishlist.auction_items.filter(item_uuid=item_pk).exists():
            wishlist.auction_items.remove(item)
        else:
            wishlist.auction_items.add(item)

        return Response(status=HTTP_200_OK)
