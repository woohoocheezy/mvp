import requests
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


# IT ISN'T USED
class Photos(APIView):
    def post(self, request, item_pk, pk):
        upload_url = ""


class GetUploadURL(APIView):
    def post(self, request):
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        url_request = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )
        url_request = url_request.json()
        return Response(url_request)
