from bootstrap_modal_forms.generic import (
    BSModalLoginView, BSModalCreateView
)
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views import View, generic

from .forms import CustomAuthenticationForm, SignupForm, AddLessonForm, EditLessonForm
from .models import Course, Lesson, Student

import datetime

User = get_user_model()


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
        course = Course.objects.filter(student_id=user.id)
        if not user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, self.template_name, context={'user': user,
                                                            'course': course})


class FinanceView(View):
    template_name = 'profile/finance.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        course = Course.objects.filter(student_id=user.id)
        if not user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, self.template_name, context={'user': user,
                                                            'course': course})


class LessonView(View):
    template_name = 'profile/lesson.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        return render(request, self.template_name, context={'user': user})


class CalendarView(View):
    template_name = 'profile/calendar.html'

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return redirect(reverse('index'))
        lessons = Lesson.objects.filter(student_id=user)
        form_add = AddLessonForm
        form_edit = EditLessonForm
        if not user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'user': user,
                                                            'form_add': form_add,
                                                            'form_edit': form_edit,
                                                            'lessons': lessons})


class AddLessonView(BSModalCreateView):
    form_class = AddLessonForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('index'))
        lesson = Lesson()
        lesson.student = Student.objects.get(user_ptr=request.user)
        lesson.subject = request.POST['subject']
        lesson.duration = request.POST['duration']
        lesson.time_start = datetime.datetime.strptime(request.POST['time_start'], '%d.%m.%Y %H:%M:%S')
        lesson.board = 'testovaya_doska'
        lesson.save()
        messages.success(self.request, 'Урок добавлен')
        return redirect(reverse('calendar'))


class EditLessonView(BSModalCreateView):
    form_class = EditLessonForm

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect(reverse('index'))
        lesson = Lesson().objects.get(id=request.id)
        print(lesson)
        # lesson.student = Student.objects.get(user_ptr=request.user)
        # lesson.subject = request.POST['subject']
        # lesson.duration = request.POST['duration']
        # lesson.time_start = datetime.datetime.strptime(request.POST['time_start'], '%d.%m.%Y %H:%M:%S')
        # lesson.board = 'testovaya_doska'
        # lesson.save()
        # messages.success(self.request, 'Урок добавлен')
        return redirect(reverse('calendar'))
