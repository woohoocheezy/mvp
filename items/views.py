from django.db import transaction
from django.db.models import (
    Q,
    BooleanField,
    Case,
    When,
    Value,
    IntegerField,
    F,
    DateField,
)
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.exceptions import (
    ParseError,
    NotFound,
    PermissionDenied,
)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from config.settings import PAGE_SIZE
from photos.serializers import PhotoSerializer
from users.models import CustomUser
from .models import FixedPriceItem, AuctionItem
from .serializers import (
    FixedPriceItemListSerializer,
    FixedPriceItemDetailSerializer,
    AuctionItemListSerializer,
    AuctionItemDetailSerializer,
)
from .filters import ItemFilter


class FixedPriceItems(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    """
    Items API URL for GET/POST request
    example : /mvp/items
    """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter

    def get(self, request):
        # print(request.user)
        """/items/?category=value
        /items/?used_years=value
        /items/?price_min=value&price_max=value
        /items/?location=value
        /items/?search=value"""

        user = request.user
        # blocked_user_ids = user.blocked_users.all()
        # print(blocked_user_ids)
        # blocked_user_ids = user.blocked_users.values_list("user_uuid", flat=True)
        # print(blocked_user_ids)
        blocked_user_ids = user.blocked_users.all().values_list("user_uuid", flat=True)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        search_query = request.query_params.get("search", "")
        categories = request.query_params.getlist("category")
        used_years = request.query_params.getlist("used_years")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        locations = request.query_params.getlist("location")

        query = Q()
        query &= Q(is_deleted=False)
        if search_query:
            query &= Q(item_name__icontains=search_query) | Q(
                description__icontains=search_query
            )
        if categories:
            query &= Q(category__in=categories)
        if used_years:
            query &= Q(used_years__in=used_years)
        if min_price:
            query &= Q(price__gte=min_price)
        if max_price:
            query &= Q(price__lte=max_price)
        if locations:
            query &= Q(location__in=locations)

        # sorting items in order by created condition
        all_items = (
            FixedPriceItem.objects.filter(query)
            .exclude(user__in=blocked_user_ids)
            .order_by("-created_at")
        )[start:end]

        serializer = FixedPriceItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        """
        from stats.models import SearchStats
        user_id = request.data.get("buy_uid")
        search_query = request.query_params.get("search", "")
        categories = request.query_params.getlist("category")
        used_years = request.query_params.getlist("used_years")
        locations = request.query_params.getlist("location")
        """

        if search_query or categories or used_years or locations:
            from stats.models import (
                SearchStats,
                SearchCategory,
                SearchLocation,
                SearchUsedYears,
            )

            # 1. Create the SearchStats instance and set the user_id.
            search_stat = SearchStats(user_id=request.user.user_uuid)
            search_stat.save()

            # 2. Handle many-to-many relationships.
            # Categories
            for category in categories:
                obj, _ = SearchCategory.objects.get_or_create(category=category)
                search_stat.searched_categories.add(obj)

            # Used Years
            for used_year in used_years:
                obj, _ = SearchUsedYears.objects.get_or_create(used_years=used_year)
                search_stat.searched_used_years.add(obj)

            # Locations
            for location in locations:
                obj, _ = SearchLocation.objects.get_or_create(location=location)
                search_stat.searched_locations.add(obj)

            search_stat.searched_keyword = search_query

            # 3. Save the SearchStats instance.
            search_stat.save()

        return Response(serializer.data)

    def post(self, request):
        request.data["user"] = request.user.user_uuid
        serializer = FixedPriceItemDetailSerializer(
            data=request.data,
            context={"request": request},
        )

        if serializer.is_valid():
            with transaction.atomic():
                item = serializer.save(user=request.user)

                photo_count = 0
                for photo_file in request.data.get("photos"):
                    serializer = PhotoSerializer(data=photo_file)

                    if serializer.is_valid():
                        photo = serializer.save(item=item)
                        if photo_count == 0:
                            photo.is_thumbnail = True
                            photo.save()
                            photo_count += 1
                        serializer = PhotoSerializer(photo)

                    else:
                        return Response(serializer.errors)

                return Response(
                    FixedPriceItemDetailSerializer(
                        item,
                        context={"request": request},
                    ).data
                )
        else:
            return Response(serializer.errors)


class FixedPriceItemDetail(APIView):

    """
    Items API URL for GET/POST/PUT/DELETE request
    example : /api/mvp/items/1
    """

    def get_object(self, pk):
        try:
            return FixedPriceItem.objects.get(pk=pk)

        except FixedPriceItem.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = FixedPriceItemDetailSerializer(
            item,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)

        data = request.data.copy()  # Create a mutable copy of request data

        serializer = FixedPriceItemDetailSerializer(
            item,
            data=data,
            partial=True,
        )

        if serializer.is_valid():
            with transaction.atomic():
                item = serializer.save()

                return Response(
                    FixedPriceItemDetailSerializer(
                        item,
                        context={"request": request},
                    ).data
                )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        item = self.get_object(pk)

        if item.is_deleted == True:
            item.is_deleted = False
        else:
            item.is_deleted = True

        serializer = FixedPriceItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = FixedPriceItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FixedPriceItemPurchase(APIView):
    """A view for changing 'is_sold' status"""

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return FixedPriceItem.objects.get(pk=pk)

        except FixedPriceItem.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)
        data = request.data.copy()

        if item.user != request.user:
            raise PermissionDenied(detail="해당 User는 수정 권한이 없음")

        if item.is_sold == True:
            item.is_sold = False
            data["buy_user"] = None
            item.buy_user = None

        else:
            item.is_sold = True

        serializer = FixedPriceItemDetailSerializer(
            item, data=data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = FixedPriceItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class FixedPriceItemDelete(APIView):
    def get_object(self, pk):
        try:
            return FixedPriceItem.objects.get(pk=pk)

        except FixedPriceItem.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)

        if item.is_deleted == True:
            item.is_deleted = False
        else:
            item.is_deleted = True

        serializer = FixedPriceItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = FixedPriceItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AuctionItems(APIView):
    # permission_classes = [IsAuthenticatedOrReadOnly]

    """
    AuctionI Items API URL for GET/POST request
    example : /mvp/items
    """

    filter_backends = (DjangoFilterBackend,)
    filterset_class = ItemFilter

    def get(self, request):
        # print(request.user)
        """/items/?category=value
        /items/?used_years=value
        /items/?price_min=value&price_max=value
        /items/?location=value
        /items/?search=value"""

        user = request.user
        blocked_user_ids = user.blocked_users.all().values_list("user_uuid", flat=True)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        search_query = request.query_params.get("search", "")
        categories = request.query_params.getlist("category")
        used_years = request.query_params.getlist("used_years")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        locations = request.query_params.getlist("location")

        query = Q()
        query &= Q(is_sold=False, is_deleted=False, is_overdue=False)
        if search_query:
            query &= Q(item_name__icontains=search_query) | Q(
                description__icontains=search_query
            )
        if categories:
            query &= Q(category__in=categories)
        if used_years:
            query &= Q(used_years__in=used_years)
        if min_price:
            query &= Q(lowest_price__gte=min_price)
        if max_price:
            query &= Q(lowest_price__lte=max_price)
        if locations:
            query &= Q(location__in=locations)

        # sorting items in order by created condition
        all_items = (
            AuctionItem.objects.filter(query)
            .exclude(user__in=blocked_user_ids)
            .order_by("deadline", "-created_at")
        )[start:end]

        serializer = AuctionItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        """
        from stats.models import SearchStats
        user_id = request.data.get("buy_uid")
        search_query = request.query_params.get("search", "")
        categories = request.query_params.getlist("category")
        used_years = request.query_params.getlist("used_years")
        locations = request.query_params.getlist("location")
        """

        """
        if search_query or categories or used_years or locations:
            from stats.models import (
                SearchStats,
                SearchCategory,
                SearchLocation,
                SearchUsedYears,
            )

            # 1. Create the SearchStats instance and set the user_id.
            search_stat = SearchStats(user_id=request.user["user_id"])
            search_stat.save()

            # 2. Handle many-to-many relationships.
            # Categories
            for category in categories:
                obj, _ = SearchCategory.objects.get_or_create(category=category)
                search_stat.searched_categories.add(obj)

            # Used Years
            for used_year in used_years:
                obj, _ = SearchUsedYears.objects.get_or_create(used_years=used_year)
                search_stat.searched_used_years.add(obj)

            # Locations
            for location in locations:
                obj, _ = SearchLocation.objects.get_or_create(location=location)
                search_stat.searched_locations.add(obj)

            search_stat.searched_keyword = search_query

            # 3. Save the SearchStats instance.
            search_stat.save()
        """

        return Response(serializer.data)

    def post(self, request):
        request.data["user"] = request.user.user_uuid
        serializer = AuctionItemDetailSerializer(
            data=request.data,
            context={"request": request},
        )

        if serializer.is_valid():
            with transaction.atomic():
                item = serializer.save(user=request.user)

                photo_count = 0
                for photo_file in request.data.get("photos"):
                    serializer = PhotoSerializer(data=photo_file)

                    if serializer.is_valid():
                        photo = serializer.save(item=item)
                        if photo_count == 0:
                            photo.is_thumbnail = True
                            photo.save()
                            photo_count += 1
                        serializer = PhotoSerializer(photo)

                    else:
                        return Response(serializer.errors)

                return Response(
                    AuctionItemDetailSerializer(
                        item,
                        context={"request": request},
                    ).data
                )
        else:
            return Response(serializer.errors)


class AuctionItemDetail(APIView):

    """
    Items API URL for GET/POST/PUT/DELETE request
    example : /api/mvp/items/1
    """

    def get_object(self, pk):
        try:
            return AuctionItem.objects.get(pk=pk)

        except AuctionItem.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = AuctionItemDetailSerializer(
            item,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)

        data = request.data.copy()  # Create a mutable copy of request data

        serializer = AuctionItemDetailSerializer(
            item,
            data=data,
            partial=True,
        )

        if serializer.is_valid():
            with transaction.atomic():
                item = serializer.save()

                return Response(
                    AuctionItemDetailSerializer(
                        item,
                        context={"request": request},
                    ).data
                )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        item = self.get_object(pk)

        if item.is_deleted is True:
            item.is_deleted = False
        else:
            item.is_deleted = True

        serializer = AuctionItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = AuctionItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AuctionItemPurchase(APIView):
    """A view for changing 'is_sold' status"""

    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return AuctionItem.objects.get(pk=pk)

        except AuctionItem.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)
        data = request.data.copy()

        if item.user != request.user:
            raise PermissionDenied(detail="해당 User는 수정 권한이 없음")

        if item.is_sold is True:
            item.is_sold = False
            data["buy_user"] = None
            item.buy_user = None
        else:
            item.is_sold = True

        serializer = AuctionItemDetailSerializer(
            item, data=data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = AuctionItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class AuctionItemDelete(APIView):
    def get_object(self, pk):
        try:
            return AuctionItem.objects.get(pk=pk)

        except AuctionItem.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)

        if item.is_deleted is True:
            item.is_deleted = False
        else:
            item.is_deleted = True

        serializer = AuctionItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = AuctionItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
