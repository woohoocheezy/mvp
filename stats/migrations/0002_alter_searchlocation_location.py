# Generated by Django 4.2.5 on 2023-11-10 05:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("stats", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="searchlocation",
            name="location",
            field=models.CharField(
                choices=[
                    ("강남구", "강남구"),
                    ("강동구", "강동구"),
                    ("강북구", "강북구"),
                    ("강서구", "강서구"),
                    ("관악구", "관악구"),
                    ("광진구", "광진구"),
                    ("구로구", "구로구"),
                    ("금천구", "금천구"),
                    ("노원구", "노원구"),
                    ("도봉구", "도봉구"),
                    ("동대문구", "동대문구"),
                    ("동작구", "동작구"),
                    ("마포구", "마포구"),
                    ("서대문구", "서대문구"),
                    ("서초구", "서초구"),
                    ("성동구", "성동구"),
                    ("성북구", "성북구"),
                    ("송파구", "송파구"),
                    ("양천구", "양천구"),
                    ("영등포구", "영등포구"),
                    ("용산구", "용산구"),
                    ("은평구", "은평구"),
                    ("종로구", "종로구"),
                    ("중구", "중구"),
                    ("중량구", "중량구"),
                    ("세종시", "세종시"),
                    ("인천시", "인천시"),
                    ("대전시", "대전시"),
                    ("광주시", "광주시"),
                    ("대구시", "대구시"),
                    ("울산시", "울산시"),
                    ("부산시", "부산시"),
                    ("경기도", "경기도"),
                    ("강원도", "강원도"),
                    ("충청북도", "충청북도"),
                    ("충청남도", "충청남도"),
                    ("전라북도", "전라북도"),
                    ("전라남도", "전라남도"),
                    ("경상북도", "경상북도"),
                    ("경상남도", "경상남도"),
                    ("제주도", "제주도"),
                ],
                max_length=10,
            ),
        ),
    ]
