# Generated by Django 4.2.4 on 2023-08-02 05:07

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ItemStatsDaily",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("total_daily_items", models.IntegerField()),
                ("nego_selected_items", models.IntegerField()),
                ("avg_selected_days_to_sell", models.IntegerField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SearchCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("가구", "가구"),
                            ("커피머신", "커피머신"),
                            ("제빙기", "제빙기"),
                            ("냉장고/냉동고", "냉장고/냉동고"),
                            ("세척기", "세척기"),
                            ("쇼케이스", "쇼케이스"),
                            ("싱크대/작업대", "싱크대/작업대"),
                            ("가스레인지/인덕션", "가스레인지/인덕션"),
                            ("포장기계", "포장기계"),
                            ("에어컨", "에어컨"),
                            ("기타", "기타"),
                        ],
                        max_length=25,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchLocation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "location",
                    models.CharField(
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
                        ],
                        max_length=10,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchUsedYears",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "used_years",
                    models.CharField(
                        choices=[
                            ("1년 이하", "1년 이하"),
                            ("1년~2년", "1년~2년"),
                            ("2년~3년", "2년~3년"),
                            ("3년~4년", "3년~4년"),
                            ("4년~5년", "4년~5년"),
                            ("5년 이상", "5년 이상"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="SearchStats",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("user_id", models.TextField(default="")),
                (
                    "searched_keyword",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "searched_categories",
                    models.ManyToManyField(blank=True, to="stats.searchcategory"),
                ),
                (
                    "searched_locations",
                    models.ManyToManyField(blank=True, to="stats.searchlocation"),
                ),
                (
                    "searched_used_years",
                    models.ManyToManyField(blank=True, to="stats.searchusedyears"),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
