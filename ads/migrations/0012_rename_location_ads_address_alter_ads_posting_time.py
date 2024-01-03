# Generated by Django 4.2 on 2024-01-03 18:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0011_seller_phone_number_alter_ads_posting_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ads',
            old_name='location',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='ads',
            name='posting_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 21, 30, 22, 432819), editable=False),
        ),
    ]