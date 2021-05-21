# Generated by Django 3.1.7 on 2021-04-19 22:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_lesson_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 4, 19, 23, 0, tzinfo=utc), verbose_name='Время'),
        ),
    ]