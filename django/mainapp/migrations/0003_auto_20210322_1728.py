# Generated by Django 3.1.7 on 2021-03-22 14:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_remove_lesson_board'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('file', models.FileField(upload_to='books')),
            ],
            options={
                'verbose_name': 'учебник',
                'verbose_name_plural': 'учебники',
            },
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 14, 0, tzinfo=utc), verbose_name='Время'),
        ),
    ]
