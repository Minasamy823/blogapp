# Generated by Django 3.0.5 on 2020-04-30 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20200430_1416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='published_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]