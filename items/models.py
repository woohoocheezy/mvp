from django.db import models
from commons.models import CommonModel
import uuid


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
        JUNGRYANG = ("중랑구", "중랑구")

        SEJONG = ("세종시", "세종시")
        INCHEON = ("인천시", "인천시")
        DAEJEON = ("대전시", "대전시")
        GWANGJU = ("광주시", "광주시")
        DAEGU = ("대구시", "대구시")
        ULSAN = ("울산시", "울산시")
        BUSAN = ("부산시", "부산시")

        GYEONGGI = ("경기도", "경기도")
        GANGWON = ("강원도", "강원도")
        CHUNGCHEONGBUK = ("충청북도", "충청북도")
        CHUNGCHEONGNAM = ("충청남도", "충청남도")
        JEOLLABUK = ("전라북도", "전라북도")
        JEOLLANAM = ("전라남도", "전라남도")
        GYEONGSANGBUK = ("경상북도", "경상북도")
        GYEONGSANGNAM = ("경상남도", "경상남도")
        JEJU = ("제주도", "제주도")

    item_uuid = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True,
    )

    user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.CASCADE,
        related_name="%(app_label)s_%(class)s_uploaded_items",
    )
    buy_user = models.ForeignKey(
        "users.CustomUser",
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_purchased_items",
        null=True,
        blank=True,
    )

    item_name = models.CharField(
        default="",
        max_length=20,
    )

    is_sold = models.BooleanField(default=False)

    is_deleted = models.BooleanField(default=False)

    # the period of use
    used_period = models.IntegerField(default=0)

    # description
    description = models.TextField()

    # category
    category = models.CharField(max_length=25, choices=CategoryChoices.choices)

    location = models.CharField(
        max_length=10, choices=LocationChoices.choices, null=True
    )

    class Meta:
        abstract = True


class FixedPriceItem(BaseItem):
    # price
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.item_name


class AuctionItem(BaseItem):
    deadline = models.DateField()
    lowest_price = models.PositiveIntegerField()
    winning_bid = models.PositiveIntegerField(null=True, blank=True)
    is_overdue = models.BooleanField(default=False)
    is_bidded = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
