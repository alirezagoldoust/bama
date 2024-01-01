# Generated by Django 4.2 on 2024-01-01 13:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_ads_posting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ads',
            name='posting_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 16, 59, 35, 685362), editable=False),
        ),
    ]
