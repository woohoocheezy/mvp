# Generated by Django 4.2.4 on 2023-09-06 01:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0003_rename_is_over_auctionitem_is_overdue_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="auctionitem",
            name="successful_bid_price",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]