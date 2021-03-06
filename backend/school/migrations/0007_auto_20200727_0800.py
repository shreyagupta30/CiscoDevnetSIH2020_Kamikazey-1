# Generated by Django 2.2.10 on 2020-07-27 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_school_district'),
    ]

    operations = [
        migrations.AddField(model_name='school', name='contact_no', field=models.CharField(blank=True, max_length=16, unique=True),),
        migrations.AddField(model_name='school', name='email', field=models.EmailField(blank=True, max_length=255, unique=True, verbose_name='email address of any school person'),),
    ]
