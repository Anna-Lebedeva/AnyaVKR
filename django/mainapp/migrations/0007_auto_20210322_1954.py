# Generated by Django 3.1.7 on 2021-03-22 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0006_book'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='grade',
            field=models.CharField(choices=[('1', '1 класс'), ('2', '2 класс'), ('3', '3 класс'), ('4', '4 класс'), ('5', '5 класс'), ('6', '6 класс'), ('7', '7 класс'), ('8', '8 класс'), ('9', '9 класс'), ('10', '10 класс'), ('11', '11 класс')], max_length=50, verbose_name='Класс'),
        ),
    ]
