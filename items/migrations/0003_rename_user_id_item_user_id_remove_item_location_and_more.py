# Generated by Django 4.2.1 on 2023-05-25 10:55

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0002_item_is_liked_item_item_name"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="user_ID",
            new_name="user_id",
        ),
        migrations.RemoveField(
            model_name="item",
            name="location",
        ),
        migrations.AlterField(
            model_name="item",
            name="category",
            field=models.CharField(
                choices=[
                    ("refrigerator", "냉장고"),
                    ("dish washer", "식기세척기"),
                    ("showcase", "쇼케이스"),
                    ("싱크", "싱크대"),
                    ("gas range", "화구/가스레인지"),
                    ("kiosk", "포스기계/키오스크"),
                    ("talbe", "테이블"),
                    ("packaging machine", "포장기계"),
                    ("air conditioner", "에어컨"),
                    ("extra", "기타"),
                ],
                max_length=25,
            ),
        ),
    ]
