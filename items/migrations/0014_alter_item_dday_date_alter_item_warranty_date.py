# Generated by Django 4.2.2 on 2023-08-02 01:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("items", "0013_alter_item_category_alter_item_warranty_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="dday_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="item",
            name="warranty_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
