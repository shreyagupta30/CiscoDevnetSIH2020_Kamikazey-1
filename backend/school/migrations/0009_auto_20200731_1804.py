# Generated by Django 2.2.10 on 2020-07-31 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0008_auto_20200727_1657'),
    ]

    operations = [
        migrations.AddField(model_name='school', name='principal', field=models.CharField(default='', max_length=50), preserve_default=False,),
        migrations.AddField(model_name='school', name='students_count', field=models.PositiveIntegerField(blank=True, default=0), preserve_default=False,),
        migrations.AddField(model_name='school', name='workers_count', field=models.PositiveIntegerField(blank=True, default=0), preserve_default=False,),
    ]
