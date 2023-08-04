import requests, mimetypes, os, imghdr
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


# IT ISN'T USED
class Photos(APIView):
    def post(self, request, item_pk, pk):
        upload_url = ""


class GetUploadURL(APIView):
    def post(self, request):
        if "file" not in request.FILES:
            return Response({"error": "No file provided"}, status=400)

        uploaded_file = request.FILES["file"]

        # Call cloudflare API for getting the upload URL
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        url_request = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )

        # Extract the upload URL from response body
        response_data = url_request.json()
        upload_url = response_data["result"]["uploadURL"]

        # Upload the file to the URL using requests
        with uploaded_file.open("rb") as f:
            file = {"file": (uploaded_file.name, f)}
            response = requests.post(upload_url, files=file)

        uploaded_url = response.json()["result"]["variants"][0]

        return Response(
            {"upload_url": uploaded_url},
            status=200,
        )
