# Generated by Django 4.2.6 on 2023-10-25 03:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_customuser_temp_user_id"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="temp_user_id",
        ),
        migrations.AlterField(
            model_name="customuser",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
