# Generated by Django 3.1.7 on 2021-03-08 00:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0013_auto_20210308_0328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.DurationField(verbose_name='Длительность занятия'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 0, 31, 32, 642838, tzinfo=utc), verbose_name='Время'),
        ),
    ]
