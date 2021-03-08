# Generated by Django 3.1.7 on 2021-03-08 00:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_auto_20210308_0352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='duration',
            field=models.CharField(choices=[(45, '45 минут'), (60, '60 минут')], default=60, max_length=50, verbose_name='Длительность занятия'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 8, 0, 56, 42, 803129, tzinfo=utc), verbose_name='Время'),
        ),
    ]
