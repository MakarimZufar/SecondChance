# Generated by Django 5.1.1 on 2024-10-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0006_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                blank=True, default="uncategorized", max_length=225, null=True
            ),
        ),
    ]
