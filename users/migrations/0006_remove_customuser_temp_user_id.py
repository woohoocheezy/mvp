# Generated by Django 4.2.5 on 2023-09-15 01:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_customuser_appled_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="temp_user_id",
        ),
    ]
