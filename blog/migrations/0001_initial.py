# Generated by Django 3.0.5 on 2020-04-29 15:10

import datetime
from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('published_at', models.DateField(default=datetime.datetime(2020, 4, 29, 15, 10, 16, 301468))),
                ('text', tinymce.models.HTMLField()),
            ],
        ),
    ]