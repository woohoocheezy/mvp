# Generated by Django 4.2.1 on 2023-05-25 04:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user",
            name="is_business_license_certificated",
        ),
        migrations.RemoveField(
            model_name="user",
            name="is_local_certificated",
        ),
        migrations.RemoveField(
            model_name="user",
            name="license_date",
        ),
        migrations.RemoveField(
            model_name="user",
            name="license_name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="license_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="name",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone_number",
        ),
        migrations.RemoveField(
            model_name="user",
            name="uuid",
        ),
    ]
