# Generated by Django 5.0.1 on 2024-02-04 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0007_alter_product_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discountPercentage',
        ),
        migrations.RemoveField(
            model_name='product',
            name='price',
        ),
        migrations.RemoveField(
            model_name='product',
            name='rating',
        ),
    ]