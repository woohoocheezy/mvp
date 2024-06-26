from django.contrib.auth.models import AnonymousUser, User
from django.conf import settings
from django.db import IntegrityError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, PermissionDenied
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.status import (
    HTTP_200_OK,
    HTTP_201_CREATED,
    HTTP_400_BAD_REQUEST,
    HTTP_204_NO_CONTENT,
)
import json, requests, random, uuid
from urllib.parse import urlparse
from botocore.exceptions import NoCredentialsError
import boto3
from config.settings import PAGE_SIZE, BUSINESS_SERVICE_KEY
from items.models import FixedPriceItem, AuctionItem
from items.serializers import (
    FixedPriceItemListSerializer,
    AuctionItemListSerializer,
    UserSoldSerializer,
)
from .models import CustomUser
from .serializers import CustomUserSerializer, BlockedUserSerailizer
from authentication.views import CustomTokenObtainPairSerializer


class UserFixedPriceItemPurchaseList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = FixedPriceItem.objects.filter(
            buy_user=request.user,
            is_sold=True,
        )[start:end]
        serializer = FixedPriceItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class UserAuctionItemPurchaseList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = AuctionItem.objects.filter(
            buy_user=request.user,
            is_sold=True,
        )[start:end]
        serializer = AuctionItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class BusinessLicense(APIView):
    def post(self, request):
        b_no = request.data.get("b_no")
        start_dt = request.data.get("start_dt")
        p_nm = request.data.get("p_nm")

        if b_no:
            if start_dt:
                if p_nm:
                    # Set the API endpoint URL
                    api_url = "https://api.odcloud.kr/api/nts-businessman/v1/validate"

                    # Set the service key (replace XXXXXXX with your actual API key)
                    service_key = f"{BUSINESS_SERVICE_KEY}"

                    data = {
                        "businesses": [
                            {
                                "b_no": b_no,
                                "start_dt": start_dt,
                                "p_nm": p_nm,
                            }
                        ]
                    }

                    # Create the headers dictionary
                    headers = {
                        "Content-Type": "application/json",
                        "Accept": "application/json",
                    }

                    # Send the request using POST method
                    response = requests.post(
                        url=api_url,
                        headers=headers,
                        params={"serviceKey": service_key},
                        data=json.dumps(data),
                    )

                    # Check the API response status code
                    if response.status_code == 200:
                        # API request successful
                        result = (
                            response.json()
                        )  # Convert the response to a JSON object
                        # print(result)  # Output the result

                        # Do any necessary data processing before sending the response to the client)
                        result = int(result["data"][0]["valid"])
                        response_data = {"result": result}

                        user = CustomUser.objects.get(user_uuid=request.user.user_uuid)
                        if result == 1:
                            user.is_certificated = True
                        else:
                            user.is_certificated = False

                        print(user.is_certificated)
                        user.save()

                        return Response(response_data)
                    else:
                        # The API request was unsuccessful
                        return Response({"error": "API request failed"})
                else:
                    # The API request was unsuccessful
                    return Response({"error": "Missing owner name"})
            else:
                # The API request was unsuccessful
                return Response({"error": "Missing start date"})
        else:
            # license_number parameter not found in request
            return Response({"error": "Missing license number"})


class UserFixedPriceItemSellingList(APIView):

    """The list of user's selling list

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = FixedPriceItem.objects.filter(
            user=request.user, is_sold=False, is_deleted=False
        )[start:end]
        serializer = FixedPriceItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class UserAuctionItemSellingList(APIView):

    """The list of user's selling list

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = AuctionItem.objects.filter(
            user=request.user, is_sold=False, is_deleted=False
        )[start:end]
        serializer = AuctionItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )

        return Response(serializer.data)


class UserSoldList(APIView):

    """The list of user's sold list

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        blocked_user_ids = request.user.blocked_users.values_list(
            "user_uuid", flat=True
        )

        queryset = list(
            FixedPriceItem.objects.filter(
                user=request.user, is_sold=True, is_deleted=False
            ).exclude(buy_user__in=blocked_user_ids)
        ) + list(
            AuctionItem.objects.filter(
                user=request.user, is_sold=True, is_deleted=False
            ).exclude(buy_user__in=blocked_user_ids)
        )
        queryset.sort(key=lambda x: x.created_at, reverse=True)
        paginated_querset = queryset[start:end]
        serializer = UserSoldSerializer(
            paginated_querset, context={"request": request}, many=True
        )

        return Response(serializer.data)


class UserCreate(APIView):
    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            random_username = uuid.uuid4().hex[:10]
            random_password = uuid.uuid4().hex[:10]
            auth_user = User.objects.create_user(
                username=random_username, password=random_password
            )
            user = serializer.save(user=auth_user)

            token_serializer = CustomTokenObtainPairSerializer(
                data={"phone_number": user.phone_number}
            )

            if token_serializer.is_valid():
                return Response(
                    token_serializer.validated_data, status=HTTP_201_CREATED
                )
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class DeleteUser(APIView):
    def delete(self, request):
        user = request.user
        user.is_deleted = True
        user.save()

        return Response(status=HTTP_204_NO_CONTENT)


class UserInformation(APIView):
    def get(self, request):
        user = request.user

        try:
            custom_user = user
            data = {
                "phone_number": custom_user.phone_number,
                "user_type": custom_user.user_type,
                "profile_image_url": custom_user.profile_image_url,
                "nick_name": custom_user.nick_name,
                "is_certificated": custom_user.is_certificated,
                "user_uuid": custom_user.user_uuid,
            }
            return Response(data, status=HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response(
                {"error": "사용자 정보가 존재하지 않습니다."}, status=HTTP_400_BAD_REQUEST
            )


class MarketingInformation(APIView):
    def get(self, request):
        user = request.user

        data = {"marketing_notification_allowed": user.marketing_notification_allowed}

        return Response(data, status=HTTP_200_OK)

    def put(self, request):
        user = request.user

        if user.marketing_notification_allowed == True:
            user.marketing_notification_allowed = False
        else:
            user.marketing_notification_allowed = True
        user.save()

        return Response(user.marketing_notification_allowed, status=HTTP_200_OK)


class PushNotification(APIView):
    def get(self, request):
        user = request.user

        data = {"chat_notification_allowed": user.chat_notification_allowed}

        return Response(data, status=HTTP_200_OK)

    def put(self, request):
        user = request.user

        if user.chat_notification_allowed == True:
            user.chat_notification_allowed = False
        else:
            user.chat_notification_allowed = True
        user.save()

        return Response(user.chat_notification_allowed, status=HTTP_200_OK)


class UpdateProfile(APIView):
    def post(self, request):
        user = request.user
        image_url = request.query_params.get("profile_image_url", None)

        if (user.profile_image_url is None) or (user.profile_image_url == ""):
            user.profile_image_url = image_url
            user.save()

            return Response(status=HTTP_200_OK)

        s3 = boto3.resource(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        parsed_url = urlparse(user.profile_image_url)
        bucket_name = parsed_url.netloc.split(".")[0]
        file_name = parsed_url.path[1:]

        # logger.info(f"{bucket_name}, {file_name}")

        try:
            s3.Object(bucket_name, file_name).delete()
        except NoCredentialsError:
            return Response({"error": "Credentials not available"}, status=400)

        user.profile_image_url = image_url
        user.save()

        return Response(status=HTTP_200_OK)


class Logout(APIView):
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        return Response(status=HTTP_200_OK)


class UpdateNickname(APIView):
    def put(self, request):
        user = request.user
        new_nick_name = request.data.get("nick_name", None)

        if not new_nick_name:
            return Response({"error": "nick_name은 필수임"}, status=HTTP_400_BAD_REQUEST)

        try:
            user.nick_name = new_nick_name
            user.save()
        except IntegrityError:
            return Response({"error": "nick_name이 중복됨"}, status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_200_OK)


class UpdatePhoneNumber(APIView):
    def put(self, request):
        user = request.user
        new_phone_number = request.data.get("phone_number", None)

        if not new_phone_number:
            return Response({"error": "phone_number는 필수임"}, status=HTTP_400_BAD_REQUEST)

        try:
            user.phone_number = new_phone_number
            user.save()
        except IntegrityError:
            return Response({"error": "phone_number가 중복됨"}, status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_200_OK)


class CheckPhoneNumber(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        phone_number = request.query_params.get("phone_number", None)

        if not phone_number:
            return Response({"error": "phone_number 필수임"}, status=HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(phone_number=phone_number).exists():
            return Response(status=HTTP_200_OK)
        else:
            return Response(
                {"error": "일치하는 phone_number가 존재하지 않음"}, status=HTTP_400_BAD_REQUEST
            )


class CheckKakaoID(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        kakao_id = request.query_parms.get("kakao_id", None)

        if not kakao_id:
            return Response({"error": "kakao_id는 필수임"}, status=HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(kakao_id=kakao_id).exists():
            return Response({"exists": True}, status=HTTP_200_OK)
        else:
            return Response({"exists": False}, status=HTTP_200_OK)


class CheckNickname(APIView):
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        nick_name = request.query_params.get("nick_name", None)

        if not nick_name:
            return Response({"error": "nick_name은 필수임"}, status=HTTP_400_BAD_REQUEST)

        if CustomUser.objects.filter(nick_name=nick_name).exists():
            return Response({"error": "nick_name이 중복됨"}, status=HTTP_400_BAD_REQUEST)

        return Response(status=HTTP_200_OK)


class UpdateFCMToken(APIView):

    """API for updating user's FCM Token

    Keyword arguments:
    argument -- description
    Return: status:200 ok or 400 bad
    """

    def put(self, request):
        user = request.user

        fcm_token = request.data.get("fcm_token", None)

        if not fcm_token:
            return Response({"error": "FCM token은 필수임"}, status=HTTP_400_BAD_REQUEST)

        user.fcm_token = fcm_token
        user.save()

        return Response(status=HTTP_200_OK)


class BlockUser(APIView):
    def post(self, request, pk):
        user_to_block = CustomUser.objects.get(user_uuid=pk)

        request.user.blocked_users.add(user_to_block)

        return Response(status=HTTP_204_NO_CONTENT)


class UnBlockUser(APIView):
    def post(self, request, pk):
        user_to_unblock = CustomUser.objects.get(user_uuid=pk)

        request.user.blocked_users.remove(user_to_unblock)

        return Response(status=HTTP_204_NO_CONTENT)


class BlockedUserList(APIView):
    def get(self, request):
        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        blocked_users = self.request.user.blocked_users.all()[start:end]

        serializer = BlockedUserSerailizer(blocked_users, many=True)

        return Response(serializer.data)
