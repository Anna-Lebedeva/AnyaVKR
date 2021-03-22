from AnyaVKR.settings import BOARD_URL  # noqa
from bootstrap_modal_forms.generic import (
    BSModalLoginView
)
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.utils.dateparse import parse_datetime
from django.views import View, generic

from .forms import CustomAuthenticationForm, SignupForm, LessonForm
from .models import Course, Lesson, Student, Teacher, Book
from ..AnyaVKR.settings import GS_BUCKET_NAME

User = get_user_model()


def define_user(u):
    if u.__class__ is Student:
        user = Student.objects.get(id=u.id)
        lessons = Lesson.objects.filter(student=user)
        is_student = True
    else:
        user = Teacher.objects.get(id=u.id)
        lessons = Lesson.objects.filter(student__student_teacher=user)
        is_student = False
    return user, lessons, is_student


def define_course(u):
    try:
        return Course.objects.get(student_id=u.id)
    except Course.DoesNotExist:
        return None


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Вы успешно вошли на сайт.'
    success_url = reverse_lazy('index')


class SignupView(SuccessMessageMixin, generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'
    success_message = 'Данные отправлены. Мы с вами свяжемся в ближайшее время!'
    success_url = reverse_lazy('index')


class ProfileView(View):
    template_name = 'profile/profile.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        user, _, is_student = define_user(user)
        course = define_course(user)
        return render(request, self.template_name, context={'user': user,
                                                            'is_student': is_student,
                                                            'course': course})


class FinanceView(View):
    template_name = 'profile/finance.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        user, _, is_student = define_user(user)
        course = define_course(user)
        return render(request, self.template_name, context={'user': user,
                                                            'is_student': is_student,
                                                            'course': course})


class LessonView(View):
    template_name = 'profile/lesson.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        user, lessons, is_student = define_user(user)
        # FIXME первый урок серьезно????
        lesson = lessons.first()
        lesson.book_id = kwargs['book']
        try:
            book_file = lesson.book.file
            print(book_file)
        except AttributeError:
            book_file = None
        bucket_name = GS_BUCKET_NAME
        return render(request, self.template_name, context={'user': user,
                                                            'is_student': is_student,
                                                            'book_file': book_file,
                                                            'BOARD_URL': BOARD_URL,
                                                            'bucket_name': bucket_name,
                                                            'lesson': lesson})


class CalendarView(View):
    template_name = 'profile/calendar.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        user, lessons, is_student = define_user(user)
        form = LessonForm
        return render(request, self.template_name, context={'user': user,
                                                            'is_student': is_student,
                                                            'form': form,
                                                            'lessons': lessons})


class CRUDLessonView(View):
    form_class = LessonForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('index'))
        if 'delete' in request.POST:
            lesson = Lesson.objects.get(student=Student.objects.get(user_ptr=request.user.id),
                                        time_start=parse_datetime(request.POST['time_start']))
            lesson.delete()
        else:
            lesson = Lesson.objects.get_or_create(student=Student.objects.get(user_ptr=request.user.id),
                                                  time_start=parse_datetime(request.POST['time_start']))[0]
            lesson.subject = request.POST['subject']
            lesson.duration = request.POST['duration']
            lesson.time_start = parse_datetime(request.POST['time_start'])
            lesson.save()
        messages.success(self.request, 'Изменения сохранены')
        return redirect(reverse('calendar'))


class BooksView(View):
    template_name = 'profile/books.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        user, _, is_student = define_user(user)
        books = Book.objects.all()
        return render(request, self.template_name, context={'user': user,
                                                            'is_student': is_student,
                                                            'books': books})
