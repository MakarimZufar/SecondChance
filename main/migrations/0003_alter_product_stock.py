# Generated by Django 5.1 on 2024-09-17 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_product_category_product_stock"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.PositiveIntegerField(default=0),
        ),
    ]