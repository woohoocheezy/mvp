# Generated by Django 4.2.5 on 2023-09-14 07:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wishlists", "0002_wishlist_temp_user_wishlistfixedpriceitem_and_more"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="wishlistfixedpriceitem",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="wishlistfixedpriceitem",
            name="item",
        ),
        migrations.RemoveField(
            model_name="wishlistfixedpriceitem",
            name="wishlist",
        ),
        migrations.DeleteModel(
            name="WishlistAuctionItem",
        ),
        migrations.DeleteModel(
            name="WishlistFixedPriceItem",
        ),
    ]
