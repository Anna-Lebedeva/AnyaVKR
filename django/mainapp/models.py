from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

grades = [
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
    ("1", _('1 занятие')),
    ("4", _('4 занятия')),
    ("7", _('7 занятий')),
    ("14", _('14 занятий')),
    ("30", _('30 занятий')),
    ("60", _('60 занятий')),
]

durations = [
    ("45", _("45 минут")),
    ("60", _("60 минут")),
]


class PreStudent(models.Model):
    first_name = models.CharField(max_length=150, verbose_name='Имя')
    phone = PhoneNumberField(region='RU', verbose_name='Телефон')
    email = models.EmailField(verbose_name='Адрес электронной почты')

    def __str__(self):
        return f'{self.first_name}, {self.phone}'

    class Meta:
        verbose_name = 'новый ученик'
        verbose_name_plural = 'новые ученики'


# TODO: при создании Ученика в админке автоматически заполнять поля Нового ученика
class Student(User):
    prestudent_id = models.ForeignKey('PreStudent', verbose_name='Заявка', on_delete=models.CASCADE, default='')
    phone = PhoneNumberField(max_length=20, region='RU', verbose_name='Телефон')
    grade = models.CharField(max_length=50, verbose_name='Класс', choices=grades)
    parent_name = models.CharField(max_length=150, verbose_name='Имя родителя', blank=True, null=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'ученик'
        verbose_name_plural = 'ученики'


class Teacher(User):
    phone = PhoneNumberField(max_length=20, region='RU', verbose_name='Телефон')
    middle_name = models.CharField(max_length=150, verbose_name='Отчество', blank=True)
    picture = models.ImageField(verbose_name='Фото', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'


class Lesson(models.Model):
    teacher_id = models.ForeignKey(Teacher, verbose_name='Преподаватель', on_delete=models.CASCADE)
    student_id = models.ForeignKey(Student, verbose_name='Ученик', on_delete=models.CASCADE)
    board = models.CharField(max_length=255, verbose_name='Идентификатор доски', default='')
    subject = models.CharField(max_length=255, verbose_name='Тема')
    time = models.DateTimeField(verbose_name='Время', default=timezone.now())
    duration = models.CharField(max_length=50, verbose_name='Длительность занятия', choices=durations)

    def __str__(self):
        return f'Учитель {self.teacher_id.first_name}, ученик {self.student_id.first_name}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Course(models.Model):
    student_id = models.ForeignKey(Student, verbose_name='Студент', on_delete=models.CASCADE, default='')
    course_length = models.CharField(max_length=50, verbose_name='Длительность курса', choices=course_lengths)

    def __str__(self):
        return f'Курс на {self.course_length} занятий'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'
