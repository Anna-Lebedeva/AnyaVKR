# Generated by Django 3.1.7 on 2021-03-03 17:57

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='student_teacher',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mainapp.teacher', verbose_name='Учитель'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 3, 17, 57, 39, 820486, tzinfo=utc), verbose_name='Время'),
        ),
    ]