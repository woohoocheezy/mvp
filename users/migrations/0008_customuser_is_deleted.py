# Generated by Django 4.2.5 on 2023-10-30 04:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_customuser_blocked_users"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="is_deleted",
            field=models.BooleanField(default=True),
        ),
    ]