# Generated by Django 5.0.1 on 2024-02-15 16:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='addresses',
        ),
        migrations.DeleteModel(
            name='Address',
        ),
    ]
