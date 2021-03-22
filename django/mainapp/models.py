import datetime

from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

User = get_user_model()

grades = [
    ("1", '1 класс'),
    ("2", '2 класс'),
    ("3", '3 класс'),
    ("4", '4 класс'),
    ("5", '5 класс'),
    ("6", '6 класс'),
    ("7", '7 класс'),
    ("8", '8 класс'),
    ("9", '9 класс'),
    ("10", '10 класс'),
    ("11", '11 класс'),
]

book_category = [
    ("oge", 'Подготовка к ОГЭ'),
    ("ege", 'Подготовка к ЕГЭ'),
    ("vpr", 'Подготовка к ВПР'),
    ("alg", 'Алгебра'),
    ("geo", 'Геометрия'),
    ("math", 'Математика'),
]

course_lengths = [
    ("1", '1 занятие'),
    ("4", '4 занятия'),
    ("7", '7 занятий'),
    ("14", '14 занятий'),
    ("30", '30 занятий'),
    ("60", '60 занятий'),
]


def hour_rounder(t):
    # Rounds to nearest hour by adding a timedelta hour if minute >= 30
    return (t.replace(second=0, microsecond=0, minute=0, hour=t.hour)
            + datetime.timedelta(hours=t.minute // 30))


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
    student_teacher = models.ForeignKey('Teacher', verbose_name='Учитель',
                                        on_delete=models.SET_NULL, null=True, blank=True)

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

    @property
    def students(self):
        return Student.objects.filter(student_teacher=self)

    @property
    def lessons(self):
        return Lesson.objects.filter(student__student_teacher=self)

    def get_full_name(self):
        return f'{self.last_name} {self.first_name} {self.middle_name}'

    class Meta:
        verbose_name = 'учитель'
        verbose_name_plural = 'учителя'


class Book(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название')
    author = models.CharField(max_length=250, verbose_name='Автор')
    file = models.FileField(upload_to='books', verbose_name='Файл')
    grade = models.CharField(max_length=50, verbose_name='Класс', choices=grades)
    category = models.CharField(max_length=50, verbose_name='Категория', choices=book_category)

    def __str__(self):
        return f'{self.grade} {self.author} {self.title}'

    class Meta:
        verbose_name = 'учебник'
        verbose_name_plural = 'учебники'


class Lesson(models.Model):
    student = models.ForeignKey(Student, verbose_name='Ученик', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255, verbose_name='Тема')
    time_start = models.DateTimeField(verbose_name='Время', default=hour_rounder(timezone.now()))
    duration = models.CharField(max_length=50, verbose_name='Длительность занятия',
                                # choices=durations,
                                default=60)
    book = models.ForeignKey(Book, verbose_name='Учебник', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'Урок id{self.id} {self.student.get_full_name()}({self.teacher.get_full_name()})'

    @property
    def teacher(self):
        return Student.objects.get(id=self.student.id).student_teacher

    @property
    def time_end(self):
        return self.time_start + datetime.timedelta(minutes=int(self.duration))

    @property
    def board(self):
        return abs(hash(str(self.student.id))) % (10 ** 8)

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
