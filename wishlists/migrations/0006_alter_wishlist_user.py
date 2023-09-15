# Generated by Django 4.2.5 on 2023-09-15 02:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_remove_customuser_temp_user_id"),
        ("wishlists", "0005_rename_temp_user_wishlist_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wishlist",
            name="user",
            field=models.ForeignKey(
                default="2009fe2b-9d93-4bd8-a773-0a25d4be5b0f",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="wishlists",
                to="users.customuser",
            ),
            preserve_default=False,
        ),
    ]
