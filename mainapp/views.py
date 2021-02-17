from bootstrap_modal_forms.generic import (
    BSModalLoginView
)
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View

from .forms import CustomAuthenticationForm

User = get_user_model()


class BaseView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')


class LoginView(BSModalLoginView):
    authentication_form = CustomAuthenticationForm
    template_name = 'registration/login.html'
    success_message = 'Вы успешно вошли на сайт.'
    success_url = reverse_lazy('index')


class ProfileView(View):

    def get(self, request, *args, **kwargs):
        user = request.user
        if not user.is_authenticated:
            return HttpResponseRedirect('/')
        return render(request, 'profile.html', context={'user': user})
