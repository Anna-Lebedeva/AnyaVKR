# Generated by Django 3.1.7 on 2021-03-22 16:45

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20210322_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название')),
                ('author', models.CharField(max_length=250, verbose_name='Автор')),
                ('file', models.FileField(upload_to='books', verbose_name='Файл')),
                ('grade', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('1', '1 класс'), ('2', '2 класс'), ('3', '3 класс'), ('4', '4 класс'), ('5', '5 класс'), ('6', '6 класс'), ('7', '7 класс'), ('8', '8 класс'), ('9', '9 класс'), ('10', '10 класс'), ('11', '11 класс')], max_length=50, verbose_name='Класс'), size=None)),
                ('category', models.CharField(choices=[('oge', 'Подготовка к ОГЭ'), ('ege', 'Подготовка к ЕГЭ'), ('vpr', 'Подготовка к ВПР'), ('alg', 'Алгебра'), ('geo', 'Геометрия'), ('math', 'Математика')], max_length=50, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'учебник',
                'verbose_name_plural': 'учебники',
            },
        ),
    ]
