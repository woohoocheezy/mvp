# Generated by Django 4.2.5 on 2023-09-15 01:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wishlists", "0003_alter_wishlistfixedpriceitem_unique_together_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="wishlist",
            name="user_id",
        ),
    ]
