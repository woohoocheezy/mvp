# Generated by Django 4.2.1 on 2023-08-08 05:58

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0015_merge_20230803_1519"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="buy_user_id",
            new_name="buy_user_uuid",
        ),
        migrations.RenameField(
            model_name="item",
            old_name="user_id",
            new_name="user_uuid",
        ),
    ]
