# Generated by Django 4.2.5 on 2023-09-14 06:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0004_customuser_temp_user_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="apple_id",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
