# Generated by Django 4.2.4 on 2023-08-29 07:37

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wishlists", "0006_rename_tempwishlist_wishlist"),
    ]

    operations = [
        migrations.RenameField(
            model_name="wishlist",
            old_name="items",
            new_name="fixed_price_items",
        ),
    ]
