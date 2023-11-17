import requests, mimetypes, os, imghdr, boto3
from uuid import uuid4
from botocore.exceptions import NoCredentialsError
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response


# IT ISN'T USED
class Photos(APIView):
    def post(self, request, item_pk, pk):
        upload_url = ""


class GetCFUploadURL(APIView):
    def post(self, request):
        # CloudFlare images upload
        if "file" not in request.FILES:
            return Response({"error": "No file provided"}, status=400)

        uploaded_file = request.FILES["file"]
        # print(uploaded_file)

        # Call cloudflare API for getting the upload URL
        url = f"https://api.cloudflare.com/client/v4/accounts/{settings.CF_ID}/images/v2/direct_upload"
        url_request = requests.post(
            url, headers={"Authorization": f"Bearer {settings.CF_TOKEN}"}
        )

        # Extract the upload URL from response body
        response_data = url_request.json()
        # print(response_data)
        upload_url = response_data["result"]["uploadURL"]

        # print(upload_url)

        # Upload the file to the URL using requests
        with uploaded_file.open("rb") as f:
            file = {"file": (uploaded_file.name, f)}
            response = requests.post(upload_url, files=file)

        uploaded_url = response.json()["result"]["variants"][0]
        # print(response.text)

        return Response(
            {"upload_url": uploaded_url},
            status=200,
        )


class GetUploadURL(APIView):
    def post(self, request):
        # S3 upload
        if "file" not in request.FILES:
            return Response({"error": "No file provided"}, status=400)

        uploaded_file = request.FILES["file"]

        # Create AWS S3 client
        s3 = boto3.client(
            "s3",
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
        )

        # Create unique file name
        file_name = str(uuid4()) + "_" + uploaded_file.name

        # Example of the file path depending on 'profile' or 'product' image
        # the case of profile
        # file_path = "profile/" + file_name

        # Upload image file to S3
        try:
            s3.upload_fileobj(
                uploaded_file,
                settings.AWS_STORAGE_BUCKET_NAME,
                uploaded_file.name,
                ExtraArgs={"ContentType": uploaded_file.content_type},
            )

        except NoCredentialsError:
            return Response({"error": "Credentials not available"}, status=400)

        uploaded_url = (
            f"https://{settings.AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/{file_name}"
        )

        return Response({"uploaded_url": uploaded_url}, status=200)
