# Generated by Django 4.2 on 2024-01-03 15:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_car_fuel_alter_ads_posting_time_alter_car_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='nardebam',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ads',
            name='posting_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 3, 18, 31, 17, 277895), editable=False),
        ),
    ]