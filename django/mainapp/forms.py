from bootstrap_modal_forms.forms import BSModalModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from .models import PreStudent, Lesson


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignupForm(forms.ModelForm):
    class Meta:
        model = PreStudent
        fields = ('first_name', 'phone', 'email')


class LessonForm(BSModalModelForm):
    duration = forms.ChoiceField(choices=[(45, "45 минут"), (60, "60 минут")], label='Длительность')
    time_start_prc = forms.DateTimeField(disabled=True, label='Начало занятия')

    class Meta:
        model = Lesson
        fields = ('subject',
                  'time_start',
                  'time_start_prc',
                  'duration')
