# Generated by Django 4.2.6 on 2023-11-29 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0010_customuser_is_deleted"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="gender",
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
