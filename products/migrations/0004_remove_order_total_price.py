# Generated by Django 5.1.2 on 2025-05-08 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_order_status_order_total_price_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="order",
            name="total_price",
        ),
    ]
