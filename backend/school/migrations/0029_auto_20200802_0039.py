# Generated by Django 2.2.10 on 2020-08-01 19:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0028_auto_20200802_0038'),
    ]

    operations = [
        migrations.AlterField(model_name='attendance', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 19, 9, 42, 882678, tzinfo=utc)),),
        migrations.AlterField(model_name='wastage', name='date', field=models.DateField(default=datetime.datetime(2020, 8, 1, 19, 9, 42, 880683, tzinfo=utc)),),
    ]
