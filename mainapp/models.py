from django import forms
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.utils.translation import gettext_lazy as _

classes = [
    ("1", _('1 класс')),
    ("2", _('2 класс')),
    ("3", _('3 класс')),
    ("4", _('4 класс')),
    ("5", _('5 класс')),
    ("6", _('6 класс')),
    ("7", _('7 класс')),
    ("8", _('8 класс')),
    ("9", _('9 класс')),
    ("10", _('10 класс')),
    ("11", _('11 класс')),
]

course_lengths = [
    ("1", _('1 день')),
    ("4", _('4 дня')),
    ("7", _('7 дней')),
    ("14", _('14 дней')),
    ("30", _('30 дней')),
    ("60", _('60 дней')),
]

#     (1, 800),
#     (4, 3000),
#     (7, 5000),
#     (14, 9200),
#     (30, 18200),
#     (60, 35000)

durations = [
    ("45", _("45 минут")),
    ("60", _("60 минут")),
]


class CustomUser(models.Model):
    username = models.CharField(max_length=150, verbose_name='Логин', unique=True)
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия', null=True)
    phone = PhoneNumberField(max_length=20, region='RU', verbose_name='Телефон')
    email = models.EmailField(max_length=255, verbose_name='Адрес электронной почты')
    password = models.password = forms.CharField(widget=forms.PasswordInput)
    is_staff = False

    class Meta:
        abstract = True

    def __str__(self):
        return self.username

    def save_user(self):
        user = User.objects.create_user(
            username=self.username, email=self.email, password=self.password, is_staff=self.is_staff)
        user.save()


class Student(CustomUser):
    year = models.CharField(max_length=50, verbose_name='Класс', choices=classes)
    parent_name = models.CharField(max_length=150, verbose_name='Имя родителя', null=True)
    course_id = models.OneToOneField('Course', verbose_name='Курс', on_delete=models.CASCADE)


class Teacher(CustomUser):
    middle_name = models.CharField(max_length=150, verbose_name='Отчество', null=True)
    picture = models.ImageField(verbose_name='Фото')
    is_staff = True


class Lesson(models.Model):
    id = models.AutoField(verbose_name='Урок', primary_key=True)
    teacher_id = models.OneToOneField('Teacher', verbose_name='Преподаватель', on_delete=models.CASCADE)
    student_id = models.ForeignKey('Student', verbose_name='Ученик', on_delete=models.CASCADE)
    board_id = models.OneToOneField('Board', verbose_name='Доска', on_delete=models.CASCADE)
    lesson_subject = models.CharField(max_length=255, verbose_name='Тема')
    date = models.DateTimeField(verbose_name='Дата')
    duration = models.CharField(max_length=50, verbose_name='Длительность занятия', choices=durations)

    def __str__(self):
        return self.id


class Board(models.Model):
    id = models.AutoField(verbose_name='Доска', primary_key=True)
    board_link = models.URLField(verbose_name='Ссылка на доску')

    def __str__(self):
        return self.board_link


class Course(models.Model):
    id = models.AutoField(verbose_name='Курс', primary_key=True)
    course_length = models.CharField(max_length=50, verbose_name='Длительность курса', choices=course_lengths)

    def __str__(self):
        return f'Курс на {self.course_length} дней'
