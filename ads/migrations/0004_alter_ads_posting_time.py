# Generated by Django 4.2 on 2024-01-01 13:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_ads_posting_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='posting_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 1, 16, 55, 12, 64417), editable=False),
        ),
    ]
