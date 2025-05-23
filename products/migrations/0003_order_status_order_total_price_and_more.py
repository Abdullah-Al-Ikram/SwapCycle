# Generated by Django 5.1.2 on 2025-05-08 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0002_pickuppoint_order"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[
                    ("pending", "Pending"),
                    ("accepted", "Accepted"),
                    ("completed", "Completed"),
                ],
                default="pending",
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="total_price",
            field=models.DecimalField(
                blank=True, decimal_places=2, max_digits=10, null=True
            ),
        ),
        migrations.AlterField(
            model_name="order",
            name="customer_name",
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name="order",
            name="phone",
            field=models.CharField(max_length=20),
        ),
    ]
