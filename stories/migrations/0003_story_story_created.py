# Generated by Django 2.0.1 on 2018-01-24 05:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20180123_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='story_created',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]