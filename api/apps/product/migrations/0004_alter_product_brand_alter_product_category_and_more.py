# Generated by Django 5.0.1 on 2024-02-04 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_image_product_thumbnail_url_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='product',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Brand',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
