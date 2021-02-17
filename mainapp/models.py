from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

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

durations = [
    ("45", _("45 минут")),
    ("60", _("60 минут")),
]


class CustomUser(User):
    phone = PhoneNumberField(max_length=20, region='RU', verbose_name='Телефон')

    class Meta:
        abstract = True


class Student(CustomUser):
    year = models.CharField(max_length=50, verbose_name='Класс', choices=classes)
    parent_name = models.CharField(max_length=150, verbose_name='Имя родителя', null=True)
    course_id = models.ForeignKey('Course', verbose_name='Курс', on_delete=models.CASCADE, related_name='course')

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Teacher(CustomUser):
    middle_name = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    picture = models.ImageField(verbose_name='Фото', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Lesson(models.Model):
    teacher_id = models.ForeignKey('Teacher', verbose_name='Преподаватель', on_delete=models.CASCADE,
                                   related_name='teacher')
    student_id = models.ForeignKey('Student', verbose_name='Ученик', on_delete=models.CASCADE, related_name='student')
    board_id = models.ForeignKey('Board', verbose_name='Доска', on_delete=models.CASCADE, related_name='board')
    lesson_subject = models.CharField(max_length=255, verbose_name='Тема')
    date = models.DateTimeField(verbose_name='Дата')
    duration = models.CharField(max_length=50, verbose_name='Длительность занятия', choices=durations)

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'lesson'
        verbose_name_plural = 'lessons'


class Board(models.Model):
    board_link = models.URLField(verbose_name='Ссылка на доску')

    def __str__(self):
        return self.board_link

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'


class Course(models.Model):
    course_length = models.CharField(max_length=50, verbose_name='Длительность курса', choices=course_lengths)

    def __str__(self):
        return f'Курс на {self.course_length} дней'

    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
