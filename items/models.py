from django.db import models
from commons.models import CommonModel
import uuid


# class Item(CommonModel):

#     """Item Model Definition"""

#     class UsedYearChoices(models.TextChoices):

#         """Used Year Choices"""

#         UNDER_1 = ("1년 이하", "1년 이하")
#         BT_1_2 = ("1년~2년", "1년~2년")
#         BT_2_3 = ("2년~3년", "2년~3년")
#         BT_3_4 = ("3년~4년", "3년~4년")
#         BT_4_4 = ("4년~5년", "4년~5년")
#         OVER_5 = ("5년 이상", "5년 이상")

#     class CategoryChoices(models.TextChoices):

#         """Category of item Choices"""

#         FURNITURE = ("가구", "가구")
#         COFFEEMACHINE = ("커피머신", "커피머신")
#         ICEMAKER = ("제빙기", "제빙기")
#         REFRIGERATOR = ("냉장고/냉동고", "냉장고/냉동고")
#         DISHWASHER = ("세척기", "세척기")
#         SHOWCASE = ("쇼케이스", "쇼케이스")
#         SINK = ("싱크대/작업대", "싱크대/작업대")
#         GASRANGE = ("가스레인지/인덕션", "가스레인지/인덕션")
#         PACKING = ("포장기계", "포장기계")
#         AIRCON = ("에어컨", "에어컨")
#         EXTRA = ("기타", "기타")

#     class LocationChoices(models.TextChoices):

#         """Location of item choices"""

#         GANGNAM = ("강남구", "강남구")
#         GANGDONG = ("강동구", "강동구")
#         GANGBUK = ("강북구", "강북구")
#         GANGSEO = ("강서구", "강서구")
#         GWANAK = ("관악구", "관악구")
#         GWANGJIN = ("광진구", "광진구")
#         GURO = ("구로구", "구로구")
#         GEUMCHEON = ("금천구", "금천구")
#         NOWON = ("노원구", "노원구")
#         DOBONG = ("도봉구", "도봉구")
#         DONGDAEMUN = ("동대문구", "동대문구")
#         DONGJAK = ("동작구", "동작구")
#         MAPO = ("마포구", "마포구")
#         SEODAEMUN = ("서대문구", "서대문구")
#         SEOCHO = ("서초구", "서초구")
#         SONGDONG = ("성동구", "성동구")
#         SONDBUK = ("성북구", "성북구")
#         SONGPA = ("송파구", "송파구")
#         YANGCHEON = ("양천구", "양천구")
#         YEOUNGDUENGPO = ("영등포구", "영등포구")
#         YONGSAN = ("용산구", "용산구")
#         EUNPYEONG = ("은평구", "은평구")
#         JONGRO = ("종로구", "종로구")
#         JUNGGU = ("중구", "중구")
#         JUNGRYANG = ("중량구", "중량구")

#     user_id = models.TextField(default="")
#     item_name = models.CharField(
#         default="",
#         max_length=20,
#     )

#     # negotiable
#     is_negotiable = models.BooleanField(
#         default=False,
#     )

#     is_sold = models.BooleanField(default=False)
#     buy_user_id = models.TextField(default="", null=True, blank=True)

#     is_deleted = models.BooleanField(default=False)

#     # price
#     price = models.PositiveIntegerField()

#     # used years
#     used_years = models.CharField(
#         max_length=20,
#         choices=UsedYearChoices.choices,
#     )

#     # manufactured date
#     manufactured_date = models.DateField(null=True, blank=True)

#     # warranty deadline
#     warranty_date = models.DateField(null=True, blank=True)

#     # description
#     description = models.TextField()

#     # category
#     category = models.CharField(max_length=25, choices=CategoryChoices.choices)

#     # about d-day
#     dday_date = models.DateField(null=True, blank=True)

#     location = models.CharField(
#         max_length=10, choices=LocationChoices.choices, null=True
#     )

#     def __str__(self):
#         return self.item_name


class BaseItem(CommonModel):

    """
    The 'Abstract Base Class' base Item model for items that have own way of
    selling like FixedPriceItem and AuctionItem.
    It contains the common fields.
    """

    class UsedYearChoices(models.TextChoices):

        """Used Year Choices"""

        UNDER_1 = ("1년 이하", "1년 이하")
        BT_1_2 = ("1년~2년", "1년~2년")
        BT_2_3 = ("2년~3년", "2년~3년")
        BT_3_4 = ("3년~4년", "3년~4년")
        BT_4_4 = ("4년~5년", "4년~5년")
        OVER_5 = ("5년 이상", "5년 이상")

    class CategoryChoices(models.TextChoices):

        """Category of item Choices"""

        FURNITURE = ("가구", "가구")
        COFFEEMACHINE = ("커피머신", "커피머신")
        ICEMAKER = ("제빙기", "제빙기")
        REFRIGERATOR = ("냉장고/냉동고", "냉장고/냉동고")
        DISHWASHER = ("세척기", "세척기")
        SHOWCASE = ("쇼케이스", "쇼케이스")
        SINK = ("싱크대/작업대", "싱크대/작업대")
        GASRANGE = ("가스레인지/인덕션", "가스레인지/인덕션")
        PACKING = ("포장기계", "포장기계")
        AIRCON = ("에어컨", "에어컨")
        EXTRA = ("기타", "기타")

    class LocationChoices(models.TextChoices):

        """Location of item choices"""

        GANGNAM = ("강남구", "강남구")
        GANGDONG = ("강동구", "강동구")
        GANGBUK = ("강북구", "강북구")
        GANGSEO = ("강서구", "강서구")
        GWANAK = ("관악구", "관악구")
        GWANGJIN = ("광진구", "광진구")
        GURO = ("구로구", "구로구")
        GEUMCHEON = ("금천구", "금천구")
        NOWON = ("노원구", "노원구")
        DOBONG = ("도봉구", "도봉구")
        DONGDAEMUN = ("동대문구", "동대문구")
        DONGJAK = ("동작구", "동작구")
        MAPO = ("마포구", "마포구")
        SEODAEMUN = ("서대문구", "서대문구")
        SEOCHO = ("서초구", "서초구")
        SONGDONG = ("성동구", "성동구")
        SONDBUK = ("성북구", "성북구")
        SONGPA = ("송파구", "송파구")
        YANGCHEON = ("양천구", "양천구")
        YEOUNGDUENGPO = ("영등포구", "영등포구")
        YONGSAN = ("용산구", "용산구")
        EUNPYEONG = ("은평구", "은평구")
        JONGRO = ("종로구", "종로구")
        JUNGGU = ("중구", "중구")
        JUNGRYANG = ("중량구", "중량구")

    item_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )
    user_id = models.TextField(default="")
    buy_user_id = models.TextField(default="", null=True, blank=True)

    item_name = models.CharField(
        default="",
        max_length=20,
    )

    is_sold = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)

    # used years
    used_years = models.CharField(
        max_length=20,
        choices=UsedYearChoices.choices,
    )

    # manufactured date
    manufactured_date = models.DateField(null=True, blank=True)
    is_manufactured = models.BooleanField(default=True)

    # description
    description = models.TextField()

    # category
    category = models.CharField(max_length=25, choices=CategoryChoices.choices)

    location = models.CharField(
        max_length=10, choices=LocationChoices.choices, null=True
    )

    temp_item_id = models.TextField(default="")
    temp_user_id = models.TextField(default="")

    class Meta:
        abstract = True


class FixedPriceItem(BaseItem):
    # price
    price = models.PositiveIntegerField()
    # negotiable
    is_negotiable = models.BooleanField(
        default=False,
    )

    def __str__(self):
        return self.item_name


class AuctionItem(BaseItem):
    # about d-day
    deadline = models.DateTimeField()
    lowest_price = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name
