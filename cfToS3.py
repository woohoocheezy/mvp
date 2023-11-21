import os
import django

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE", "config.settings"
)  # myproject.settings를 프로젝트의 settings.py 파일 경로로 변경해주세요.
django.setup()

import requests, boto3
from photos.models import Photo
from config.settings import (
    AWS_STORAGE_BUCKET_NAME,
    AWS_SECRET_ACCESS_KEY,
    AWS_ACCESS_KEY,
)

s3 = boto3.client(
    "s3",
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name="ap-northeast-2",  # 예: 'ap-northeast-2' (서울)
)

# photos = Photo.objects.all()

# for photo in photos:
#     response = requests.get(photo.file)

#     if response.status_code != 200:
#         # print(photo.photo_uuid)
#         print(photo.photo_uuid, photo.file)

#     # print(response.)
#     file_name = photo.file.split("/")[-2]

#     s3_bucket_name = AWS_STORAGE_BUCKET_NAME

#     s3.put_object(Body=response.content, Bucket=s3_bucket_name, Key=file_name)

#     new_url = f"https://{s3_bucket_name}.s3.ap-northeast-2.amazonaws.com/{file_name}"
#     photo.file = new_url
#     photo.save()


from users.models import CustomUser

users = CustomUser.objects.all()

for user in users:
    # print(user.profile_image_url)
    if (user.profile_image_url is not None) and (user.profile_image_url != ""):
        print(user.profile_image_url, end=" ")

        response = requests.get(user.profile_image_url)

        file_name = "userprofle" + str(user.user_uuid)

        s3_bucket_name = AWS_STORAGE_BUCKET_NAME

        s3.put_object(Body=response.content, Bucket=s3_bucket_name, Key=file_name)

        new_url = (
            f"https://{s3_bucket_name}.s3.ap-northeast-2.amazonaws.com/{file_name}"
        )
        user.profile_image_url = new_url
        user.save()
        print(user.profile_image_url)


# from chats.models import Message

# messages = Message.objects.filter(type="image")
# print("messages")
# for message in messages:
#     # print(message.image)
#     print(message.image, end=" ")

#     response = requests.get(message.image)

#     # print(response.)
#     file_name = message.image.split("/")[-2]

#     s3_bucket_name = AWS_STORAGE_BUCKET_NAME

#     s3.put_object(Body=response.content, Bucket=s3_bucket_name, Key=file_name)

#     new_url = f"https://{s3_bucket_name}.s3.ap-northeast-2.amazonaws.com/{file_name}"
#     message.image = new_url
#     message.save()

#     print(message.image)
