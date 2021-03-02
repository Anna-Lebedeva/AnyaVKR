from bootstrap_modal_forms.generic import (
    BSModalLoginView
)
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View, generic

from .forms import CustomAuthenticationForm, SignupForm
from .models import Course, Lesson

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
        lesson = Lesson.objects.filter(student_id=user.id)
        if not user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, self.template_name, context={'user': user,
                                                            'course': course,
                                                            'lesson': lesson})
