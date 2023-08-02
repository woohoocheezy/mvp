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
)

# from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from config.settings import PAGE_SIZE
from photos.serializers import PhotoSerializer
from .models import Item
from .serializers import ItemListSerializer, ItemDetailSerializer
from .filters import ItemFilter


class Items(APIView):
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

        # info = f'METHOD: {request.method}\n'
        # info += f'URL: {request.get_full_path()}\n'
        # info += f'GET: {request.GET}\n'
        # info += f'POST: {request.POST}\n'
        # info += f'COOKIES: {request.COOKIES}\n'
        # info += f'META: {request.META}\n'

        # print(info)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size
        # print(f"request.query_params : {request.query_params}")
        search_query = request.query_params.get("search", "")
        # category = request.query_params.get("category")
        categories = request.query_params.getlist("category")
        # used_years = request.query_params.get("used_years")
        used_years = request.query_params.getlist("used_years")
        min_price = request.query_params.get("min_price")
        max_price = request.query_params.get("max_price")
        # location = request.query_params.get("location")
        locations = request.query_params.getlist("location")
        # print(f"search_query : {search_query}")
        # print(used_years)

        query = Q()
        query &= Q(is_sold=False, is_deleted=False)
        if search_query:
            query &= Q(item_name__icontains=search_query) | Q(
                description__icontains=search_query
            )
        # if category:
        #     query &= Q(category__icontains=category)
        if categories:
            query &= Q(category__in=categories)
        if used_years:
            query &= Q(used_years__in=used_years)
        if min_price:
            query &= Q(price__gte=min_price)
        if max_price:
            query &= Q(price__lte=max_price)
        # if location:
        #     query &= Q(location__icontains=location)
        if locations:
            query &= Q(location__in=locations)

        # if search_query:
        #     all_items = Item.objects.filter(
        #         Q(item_name__icontains=search_query)
        #         | Q(item_description__icontains=search_query)
        #     )[start:end]
        # else:
        #     all_items = Item.objects.all()[start:end]

        """test"""
        # test1 = Item.objects.filter(query).filter("dday_date").order_by("dday_date","-created_at")
        # test2 = Item.objects.filter(query).filter().order_by("-created_at")

        # all_items = test1 + test2
        # all_items = all_items[start:end]
        """test end"""


        now = timezone.now().date()

        # 적용되던 코드 very important
        # all_items = Item.objects.filter(query).order_by("dday_date","-created_at")[start:end] 

        # sorting items in order by created condition
        all_items = (
            Item.objects.filter(query)
            .annotate(
                order_priority=Case(
                    When(dday_date__lte=now, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                ),
                # Use dday_date if dday_date is today or later, otherwise use now.
                custom_date=Case(
                    When(dday_date__gt=now, then=F("dday_date")),
                    default=Value(now),
                    output_field=DateField(),
                ),
            )
            .order_by("order_priority", "custom_date", "-created_at")
        )[start:end]


        serializer = ItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )
        # print(serializer.data)
        # print("hi")
        # print(request.user['user_id'])

        """
        from stats.models import SearchStats
        user_id = request.data.get("buy_uid")
        search_query = request.query_params.get("search", "")
        categories = request.query_params.getlist("category")
        used_years = request.query_params.getlist("used_years")
        locations = request.query_params.getlist("location")
        """

        if search_query or categories or used_years or locations:
        
            from stats.models import SearchStats, SearchCategory, SearchLocation, SearchUsedYears
            
            # 1. Create the SearchStats instance and set the user_id.
            search_stat = SearchStats(user_id=request.user['user_id'])
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
        serializer = ItemDetailSerializer(
            data=request.data,
            context={"request": request},
        )
        # print(request.user.get("uid"))
        # serializer.user_id = request.user.get("uid")

        # print(request.data.get("photos[0]"))
        # print()
        # print(type((request.data.get("photos[1]"))))

        if serializer.is_valid():
            # user_pk = request.data.get("user_id")

            # if not user_pk:
            #     raise ParseError("user_id is requried")

            with transaction.atomic():
                serializer.pho = request.user.get("uid")
                item = serializer.save()
                # print(item.pk)
                # print(request.data.get("photos"))

                for photo_file in request.data.get("photos"):
                    # print(type(photo_file), photo_file)

                    serializer = PhotoSerializer(data=photo_file)

                    if serializer.is_valid():
                        photo = serializer.save(item=item)
                        serializer = PhotoSerializer(photo)

                    else:
                        return Response(serializer.errors)

                return Response(
                    ItemDetailSerializer(
                        item,
                        context={"request": request},
                    ).data
                )
        else:
            return Response(serializer.errors)

        # class ItemPhotos(APIView):
        #     def get_object(self, pk):
        #         try:
        #             return Item.objects.get(pk=pk)
        #         except Item.DoesNotExist:
        #             raise NotFound

        #     def post(self, request, pk):
        #         print(request.data)

        """Doesn't work"""
        # item = self.get_object(pk)

        # serializer = PhotoSerializer(data=request.data)
        # # print(request.data)

        # if serializer.is_valid():
        #     photo = serializer.save(item=item)
        #     serializer = PhotoSerializer(photo)
        #     return Response(serializer.data)
        # else:
        #     return Response(serializer.errors)


class ItemDetail(APIView):

    """
    Items API URL for GET/POST/PUT/DELETE request
    example : /api/mvp/items/1
    """

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)

        except Item.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        item = self.get_object(pk)
        serializer = ItemDetailSerializer(
            item,
            context={"request": request},
        )
        return Response(serializer.data)

    def put(self, request, pk):
        item = self.get_object(pk)

        data = request.data.copy()  # Create a mutable copy of request data
        if "dday_date" in data:
            data.pop("dday_date")  # Remove 'd-day' from the data if it exists

        serializer = ItemDetailSerializer(
            item,
            data=data,
            partial=True,
        )

        if serializer.is_valid():
            # user_pk = request.data.get("user_id")

            # if not user_pk:
            #     raise ParseError("user_id is requried")

            with transaction.atomic():
                item = serializer.save()

                return Response(
                    ItemDetailSerializer(
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

        serializer = ItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = ItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ItemPurchase(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)

        except Item.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)

        print(request.data.get("buy_uid"))

        if item.is_sold == True:
            item.is_sold = False
            item.buy_user_id = ""
        else:
            item.is_sold = True
            item.buy_user_id = request.data.get("buy_uid")

        serializer = ItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = ItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class ItemDelete(APIView):
    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)

        except Item.DoesNotExist:
            raise NotFound

    def put(self, request, pk):
        item = self.get_object(pk)

        if item.is_deleted == True:
            item.is_deleted = False
        else:
            item.is_deleted = True

        serializer = ItemDetailSerializer(
            item, data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            item = serializer.save()
            item = ItemDetailSerializer(item)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
