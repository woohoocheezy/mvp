# Generated by Django 4.2.6 on 2023-10-30 04:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0009_remove_customuser_temp_user_id_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_deleted",
            field=models.BooleanField(default=False),
        ),
    ]