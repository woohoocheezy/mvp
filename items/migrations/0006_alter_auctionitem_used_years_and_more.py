# Generated by Django 4.2.6 on 2023-11-11 01:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0005_auctionitem_used_period_fixedpriceitem_used_period"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auctionitem",
            name="used_years",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1년 이하", "1년 이하"),
                    ("1년~2년", "1년~2년"),
                    ("2년~3년", "2년~3년"),
                    ("3년~4년", "3년~4년"),
                    ("4년~5년", "4년~5년"),
                    ("5년 이상", "5년 이상"),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="fixedpriceitem",
            name="used_years",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1년 이하", "1년 이하"),
                    ("1년~2년", "1년~2년"),
                    ("2년~3년", "2년~3년"),
                    ("3년~4년", "3년~4년"),
                    ("4년~5년", "4년~5년"),
                    ("5년 이상", "5년 이상"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
