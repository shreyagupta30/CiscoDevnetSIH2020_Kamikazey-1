# Generated by Django 2.2.10 on 2020-08-03 00:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0033_auto_20200803_0424'),
    ]

    operations = [
        migrations.AlterField(model_name='filehash', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 8, 3, 5, 48, 19, 430899)),),
    ]
