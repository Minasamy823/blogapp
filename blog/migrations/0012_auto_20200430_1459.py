# Generated by Django 3.0.5 on 2020-04-30 14:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200430_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 4, 30, 14, 59, 50, 949078, tzinfo=utc)),
        ),
    ]
