# Generated by Django 4.2.1 on 2023-07-02 09:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0011_alter_item_buy_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="dday_date",
            field=models.DateField(default="1970-01-01"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="item",
            name="manufactured_date",
            field=models.DateField(default="1970-01-01"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="item",
            name="warranty_date",
            field=models.DateField(default="1970-01-01"),
            preserve_default=False,
        ),
    ]
