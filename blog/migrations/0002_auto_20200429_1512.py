# Generated by Django 3.0.5 on 2020-04-29 15:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateField(default=datetime.datetime(2020, 4, 29, 15, 12, 5, 554354, tzinfo=utc)),
        ),
    ]