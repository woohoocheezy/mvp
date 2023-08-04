from django.contrib.auth.models import AnonymousUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, PermissionDenied
from items.models import Item
from items.serializers import ItemListSerializer
from config.settings import PAGE_SIZE, BUSINESS_SERVICE_KEY
import requests, json


class UserPurchaseList(APIView):
    def get(self, request):
        # print(request.user.get("uid"))

        user_id = request.user.get("uid")

        if not user_id:
            return Response(PermissionDenied)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = Item.objects.filter(
            buy_user_id=user_id, is_sold=True, is_deleted=False
        )[start:end]
        serializer = ItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )
        # print(serializer.data)

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

                    # Set the data as a dictionary
                    # data = {
                    #     "businesses": [
                    #         {
                    #             "b_no": "1222936420",
                    #             "start_dt": "20110901",
                    #             "p_nm": "이정희",
                    #         }
                    #     ]
                    # }

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
                        print(result)  # Output the result
                    else:
                        # API request failed
                        print(response.status_code)  # Output the HTTP status code
                        print(response.text)  # Output the response body

                    if response.status_code == 200:
                        # Do any necessary data processing before sending the response to the client)
                        result = int(result["data"][0]["valid"])
                        response_data = {"result": result}
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


class UserSellingList(APIView):

    """The list of user's selling list

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def get(self, request):
        # print(request.user.get("uid"))

        user_id = request.user.get("uid")

        if not user_id:
            return Response(PermissionDenied)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = Item.objects.filter(
            user_id=user_id, is_sold=False, is_deleted=False
        )[start:end]

        serializer = ItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )
        # print(serializer.data)

        return Response(serializer.data)


class UserSoldList(APIView):

    """The list of user's sold list

    Keyword arguments:
    argument -- description
    Return: return_description
    """

    def get(self, request):
        # print(request.user.get("uid"))
        # print(request.user, type(request.user))

        if type(request.user) == AnonymousUser:
            return Response(PermissionDenied)

        user_id = request.user.get("uid")
        # print(user_id)

        if not user_id:
            return Response(PermissionDenied)

        try:
            page = int(request.query_params.get("page", 1))
        except ValueError:
            page = 1

        page_size = PAGE_SIZE
        start = (page - 1) * page_size
        end = start + page_size

        all_items = Item.objects.filter(
            user_id=user_id, is_sold=True, is_deleted=False
        )[start:end]

        serializer = ItemListSerializer(
            all_items,
            many=True,
            context={"request": request},
        )
        # print(serializer.data)

        return Response(serializer.data)


# class Users(APIView):

#     """APIView for creating a user
#     ex) 'POST /uesrs' request handler
#     """

#     def post(self, request):
#         """POST /users' handler to create a user

#         Keyword arguments:
#         request -- the request from user
#         Return: the created user
#         """

#         # password validation
#         password = request.data.get("password")
#         if not password:
#             raise ParseError

#         serializer = PrivateUserSerializer(data=request.data)

#         if serializer.is_valid():
#             user = serializer.save()
#             user.set_password(password)
#             user.save()

#             serializer = PrivateUserSerializer(user)

#             return Response(serializer.data)

#         else:
#             return Response(serializer.errors)
