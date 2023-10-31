from items.models import FixedPriceItem
import csv
from users.models import CustomUser
from photos.models import Photo


def fixed_new():
    fixed_csv_file = "fixed results.csv"

    user = CustomUser.objects.get(nick_name="트레져")

    with open(fixed_csv_file, "r") as file:
        csv_reader = csv.reader(file, delimiter=",")

        for row in csv_reader:
            item = FixedPriceItem(
                user=user,
                item_name=row[5],
                is_sold=True,
                used_years=row[8],
                manufactured_date=row[9],
                is_manufactured=row[10],
                description=row[11],
                category=row[12],
                location=row[13],
                price=row[14],
                is_negotiable=row[15],
            )
            item.save()
            item.created_at = row[0]
            item.save()

            csv_file = "photo results.csv"
            with open(csv_file, "r") as file:
                # CSV 파일 읽기
                photo_csv_reader = csv.reader(file, delimiter=",")

                # 각 줄을 띄어쓰기로 대체하여 출력
                for photo_row in photo_csv_reader:
                    if str(photo_row[4]) == row[2]:
                        # print(row[4], row[3], row[6])
                        photo = Photo.objects.create(
                            file=photo_row[3],
                            item=item,
                        )
                        if photo_row[6] == "1":
                            photo.is_thumbnail = True
                            photo.save()
