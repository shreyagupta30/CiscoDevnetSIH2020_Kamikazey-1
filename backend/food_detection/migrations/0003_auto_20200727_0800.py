# Generated by Django 2.2.10 on 2020-07-27 02:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0002_auto_20200726_2332'),
    ]

    operations = [
        migrations.AlterField(model_name='filehash', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 7, 27, 8, 0, 33, 606044)),),
    ]
