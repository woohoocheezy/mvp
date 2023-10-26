from photos.models import Photo
from items.models import FixedPriceItem, AuctionItem
import csv

fixed_data = """
42c59265ce4b4cd5892e38a636dec76c, 애견샵 유리장 28개, 2b6d25b2-7672-44f4-81c8-72c75a1aa7a9
4c6dd2f506344644bdeb7e3a08fe7b48, 우성 업소용 냉장고, 2ec32673-2dd2-45a1-a2d6-26008006297a
51c09a6c55b145c385cf5f60fb69205f, 음료 쇼케이스, 7aedb2af-9379-4f42-8ab6-7e5aa54db6a4
555ddd0fcc0448cd928895274aa6d067, 우성 냉장/냉동고45박스, f760e36c-8f90-4869-98d1-97f8e4d269be
64e72401eef941d990862f4b1a8ffb8e, 냉동 쇼케이스, 00a2286f-a90d-45d2-b253-0d9c87951b6a
88e1d54f26c1410db887688ba7cc1f4d, 우성 냉장고 올냉장, 76b7867e-9658-420a-bffe-7ebcf7e33382
8be481a1ce7440d8a58a1d0b239ce1f1, 우성 수직냉동 쇼케이스, 50a9f211-fd64-4cad-b53c-865236f2d9a1
8d68e4d31cc34a99a9c4409a9dbc32c9, 스키피오 음료 쇼케이스, 2cab1cca-1329-4572-bf77-1db2e035ad87
ba768589404e4319bee5bcd8b970491b, 에이플러스 애견 드라이어 6개, 41e3efc5-582a-4de1-b37d-92233d0745b3
be26e6926c2c4bc19bcdce0dd2327cea, 시디즈 T50 화이트쉘 메쉬의자, d3194e77-c99e-4773-a6ce-e4455c853f3c
c3aa476da2704a618080cbca26c22480, 프로맥 그린미 플러스 커피머신 2그룹, eecdd6ee-a429-45f8-acdc-5a99e0a5eccb
c3cd3989f5f843b1ab3f98d9c677df5f, 포스뱅크 포스기, ba2f8d31-a1c7-4db6-91e0-36718f8869fd
d11d170ee432429a902f836d447b8c09, 그랜드우성 쇼케이스, 8e63e264-87d1-4426-99cb-479cb9b398c9
d7491f475818451e8dfa9af080c9da32, SKIPIO 냉동쇼케이스, b348b322-6efe-42d3-9db0-5f8ec6b59e0c
ddb1157d9cf64570a27e1894f6e92aa8, 4단 쇼케이스, 1eafeb86-77b5-4fa6-b37e-f0b026d91058
eeba8171a2264e71a143273056c1e000, 실링 랩칼 4000개, c359395d-e874-4487-9cbd-21ce74b656ce
f890d43dfdc446a69c8c475b693248e5, 깡통 테이블 8개, 77dbb624-9409-4191-b79b-a0fd9ddd4a86
fafcec1b036e478da36ac73f07918c5b, 브레마 제빙기, 2005e3b1-79d9-4de4-8558-ccfa9fd289eb
""".strip().split(
    "\n"
)

fixed_dict = {line.split(", ")[0]: line.split(", ")[-1] for line in fixed_data}

fixed_items = [
    "42c59265ce4b4cd5892e38a636dec76c",
    "4c6dd2f506344644bdeb7e3a08fe7b48",
    "51c09a6c55b145c385cf5f60fb69205f",
    "555ddd0fcc0448cd928895274aa6d067",
    "64e72401eef941d990862f4b1a8ffb8e",
    "88e1d54f26c1410db887688ba7cc1f4d",
    "8be481a1ce7440d8a58a1d0b239ce1f1",
    "8d68e4d31cc34a99a9c4409a9dbc32c9",
    "ba768589404e4319bee5bcd8b970491b",
    "be26e6926c2c4bc19bcdce0dd2327cea",
    "c3aa476da2704a618080cbca26c22480",
    "c3cd3989f5f843b1ab3f98d9c677df5f",
    "d11d170ee432429a902f836d447b8c09",
    "d7491f475818451e8dfa9af080c9da32",
    "ddb1157d9cf64570a27e1894f6e92aa8",
    "eeba8171a2264e71a143273056c1e000",
    "f890d43dfdc446a69c8c475b693248e5",
    "fafcec1b036e478da36ac73f07918c5b",
]


def fixed_photo_migrate():
    csv_file = "photo results.csv"

    # CSV 파일 열기
    with open(csv_file, "r") as file:
        # CSV 파일 읽기
        csv_reader = csv.reader(file, delimiter=",")

        # 각 줄을 띄어쓰기로 대체하여 출력
        for row in csv_reader:
            if str(row[4]) in fixed_items:
                # print(row[4], row[3], row[6])
                item = FixedPriceItem.objects.get(item_uuid=fixed_dict[row[4]])
                photo = Photo.objects.create(
                    file=row[3],
                    item=item,
                )
                if row[6] == "1":
                    photo.is_thumbnail = True
                    photo.save()


auction_data = """
13e25560a4d6413995bfbb95e11b221a, db4bf31d-1f50-40a8-9d17-05fed70704d4, 린나이 하향식 저장식 온수기
48e00fef8a1948b3afea1dc540a91dac, ed552042-cc70-4441-87a1-d3efd046ec01, 테이블	
585d5960478844949d04950a07080b0d, 5481d341-e2e8-4f61-8ce5-a7d8f5e225f4, 소파 2개
6618625714e946ab8fe471895d7c1dee, 2c29667a-e481-490b-8ba6-3e24d2fa3f65, 씨메 05 시그니처 화이트 커피머신
6fab895df5a148c5a08f25f1b84b02e9, c58b6074-a5c6-4406-8a20-a3998aea43be, 위니아 세탁기 15kg
a6febde329a5479cb1f959af8576771b, a2591ebd-e195-45fa-afaf-e44da3d13a47, 카이저 제빙기 110kg
ada119b6af014d4995063802b5131826, bb94e4b6-0d35-41ab-be66-a65a814bf81e, 루베크 후드 믹서
""".strip().split(
    "\n"
)

auction_dict = {line.split(", ")[0]: line.split(", ")[1] for line in auction_data}

auction_items = [
    "13e25560a4d6413995bfbb95e11b221a",
    "48e00fef8a1948b3afea1dc540a91dac",
    "585d5960478844949d04950a07080b0d",
    "6618625714e946ab8fe471895d7c1dee",
    "6fab895df5a148c5a08f25f1b84b02e9",
    "a6febde329a5479cb1f959af8576771b",
    "ada119b6af014d4995063802b5131826",
]


def auction_photo_migrate():
    csv_file = "photo results.csv"

    # CSV 파일 열기
    with open(csv_file, "r") as file:
        # CSV 파일 읽기
        csv_reader = csv.reader(file, delimiter=",")

        # 각 줄을 띄어쓰기로 대체하여 출력
        for row in csv_reader:
            if str(row[4]) in auction_items:
                # print(row[4], row[3], row[6])
                item = AuctionItem.objects.get(item_uuid=auction_dict[row[4]])
                photo = Photo.objects.create(
                    file=row[3],
                    item=item,
                )
                if row[6] == "1":
                    photo.is_thumbnail = True
                    photo.save()
