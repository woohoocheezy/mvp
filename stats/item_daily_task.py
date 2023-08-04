#! /home/woohoocheezy/.cache/pypoetry/virtualenvs/spacejump-736Ebgb5-py3.10/bin/python3
import os
import sys
from django import setup

# Add project root directory to sys.path
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
setup()

from django.core.management.base import BaseCommand
from django.utils.timezone import localtime, now, make_aware
from items.models import Item
from stats.models import ItemStatsDaily
from datetime import datetime, timedelta
from django.db.models import Q

# import logging

# log_filename = "/home/woohoocheezy/sosang-mvp/stats/analyze_daily_data.log"
# logging.basicConfig(filename=log_filename, level=logging.INFO)


def analyze_daily_data():
    help = 'Fetch data from "items" model and process & analyze it daily'

    # get all posts created at yesterday
    today = datetime.now().date()
    yesterday = today - timedelta(days=1)

    yesterday_start = make_aware(datetime.combine(yesterday, datetime.min.time()))
    yesterday_end = make_aware(datetime.combine(yesterday, datetime.max.time()))

    yesterday_records = Item.objects.filter(
        Q(created_at__range=(yesterday_start, yesterday_end))
    )

    if len(yesterday_records) != 0:
        daily_items_count = len(yesterday_records)
        # print(f"daily_items_count: {daily_items_count}")
        nego_selected_items_count = analyze_nego_count(yesterday_records)
        # print(f"nego_selected_items_count: {nego_selected_items_count}")
        selected_days_to_sell_avg = analyze_dday_avg(yesterday_records)
        # print(f"selected_days_to_sell_avg: {selected_days_to_sell_avg}")
        # popular_category = analyze_category_data(yesterday_records)
        # print(f"popular_category: {popular_category}")

        itemstats = ItemStatsDaily(
            total_daily_items=daily_items_count,
            nego_selected_items=nego_selected_items_count,
            avg_selected_days_to_sell=selected_days_to_sell_avg,
        )
        itemstats.save()

        print(f"Script executed at {datetime.now()}")
        # analyze_dday_avg_check(yesterday_records)
    else:
        print(f"Script executed failed [no yesterday records] at {datetime.now()}")


def analyze_dday_avg_check(records):
    from django.db.models import Avg, F

    today = datetime.now().date()

    # annotate() 함수를 사용하여 days_to_dday 필드를 추가합니다.
    annotated_records = records.annotate(days_to_dday=F("dday_date") - today)

    # annotated_records의 객체별로 days_to_dday를 출력합니다.
    # for record in annotated_records:
    #     print(f"[{record.id}] Days to D-Day: {record.days_to_dday}")

    # days_to_dday의 평균을 계산합니다.
    average_dday = annotated_records.aggregate(Avg("days_to_dday"))

    average_days_to_dday = average_dday["days_to_dday__avg"].days
    return average_days_to_dday


def analyze_dday_avg(records):
    from django.db.models import Avg, F

    today = datetime.now().date()

    average_dday = records.annotate(days_to_dday=F("dday_date") - today).aggregate(
        Avg("days_to_dday")
    )

    average_days_to_dday = average_dday["days_to_dday__avg"].days
    return average_days_to_dday

    """
    from django.db.models import Avg, ExpressionWrapper, F, DateField

    import datetime

    today = datetime.datetime.now().date()
    print(today)
    print(records[0].dday_date)

    # average_dday = records.annotate(
    #     days_to_dday=ExpressionWrapper(today - F("dday_date"), output_field=DateField())
    # ).aggregate(Avg("days_to_dday"))
    average_dday = records.annotate(
        days_to_dday=((F("dday_date") - today) / timedelta(days=1))
    ).aggregate(Avg("days_to_dday"))

    print(average_dday)
    average_days_to_dday = average_dday["days_to_dday__avg"]

    return average_days_to_dday
    """


def analyze_nego_count(records):
    nego_items_count = records.filter(is_negotiable=True).count()

    return nego_items_count


def analyze_category_data(records):
    """
    analyze the category data
    for the most common category for yesterday
    """

    # calculate the most common category
    from django.db.models import Count

    most_common_category = (
        records.values("category")
        .annotate(count=Count("category"))
        .order_by("-count")
        .first()
    )
    most_common_category_name = most_common_category["category"]

    return most_common_category_name


if __name__ == "__main__":
    """
    from django.utils import timezone

    items = Item.objects.all()
    print(items[46].created_at)
    # 현재 시간을 얻습니다.
    now = timezone.now()

    # 어제 날짜를 구합니다
    yesterday = now - timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    # Item 객체를 가져옵니다.
    items = Item.objects.all()

    # items[49]의 created_at을 어제날짜로 변경합니다.
    item_to_update = items[46]
    item_to_update.created_at = yesterday

    # 변경 사항을 저장합니다.
    item_to_update.save()

    # 변경된 created_at을 출력합니다.
    print(items[46].created_at)
    """
    print()

    analyze_daily_data()
