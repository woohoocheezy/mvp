from django.core.management.base import BaseCommand
from django.core.mail import EmailMessage
from django.http import HttpResponse
from users.models import CustomUser
import csv


class Command(BaseCommand):
    help = "Send an email with the CSV attachment"

    def handle(self, *args, **kwargs):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="users.csv"'
        writer = csv.writer(response)
        fields = [
            "nick_name",
            "name",
            "sector",
            "user_type",
            "phone_number",
            "create_at",
            "chat_notification_allowed",
            "marketing_notification_allowed",
            "is_certificated",
            "is_deleted",
            "birth_date",
        ]
        writer.writerow(fields)
        queryset = CustomUser.objects.all().order_by("create_at")
        for user in queryset:
            row = writer.writerow([getattr(user, field) for field in fields])

        # 파일로 저장
        with open("users.csv", "w", newline="") as f:
            f.write(response.content.decode())

        email = EmailMessage(
            "유저 데이터",  # 제목
            "유저 데이터입니다",  # 내용
            "housedabang@gmail.com",  # 보내는 사람
            [
                "preemi65@gmail.com",
            ],  # 받는 사람
            headers={"Message-ID": "foo"},
        )

        # CSV 파일 첨부 후 이메일 전송
        email.attach_file("users.csv")
        email.send()
