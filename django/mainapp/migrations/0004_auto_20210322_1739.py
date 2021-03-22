# Generated by Django 3.1.7 on 2021-03-22 14:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20210322_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(blank=True, choices=[('oge', 'Подготовка к ОГЭ'), ('ege', 'Подготовка к ЕГЭ'), ('vpr', 'Подготовка к ВПР'), ('alg', 'Алгебра'), ('geo', 'Геометрия'), ('math', 'Математика')], max_length=50, null=True, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='book',
            name='grade',
            field=models.CharField(blank=True, choices=[('1', '1 класс'), ('2', '2 класс'), ('3', '3 класс'), ('4', '4 класс'), ('5', '5 класс'), ('6', '6 класс'), ('7', '7 класс'), ('8', '8 класс'), ('9', '9 класс'), ('10', '10 класс'), ('11', '11 класс')], max_length=50, null=True, verbose_name='Класс'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='time_start',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 22, 15, 0, tzinfo=utc), verbose_name='Время'),
        ),
    ]
