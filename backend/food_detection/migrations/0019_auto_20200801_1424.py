# Generated by Django 2.2.10 on 2020-08-01 08:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food_detection', '0018_auto_20200801_1418'),
    ]

    operations = [
        migrations.AlterField(model_name='filehash', name='datetime', field=models.DateTimeField(default=datetime.datetime(2020, 8, 1, 14, 24, 24, 153522)),),
    ]