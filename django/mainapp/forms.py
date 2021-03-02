from bootstrap_modal_forms.forms import BSModalForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

from mainapp.models import PreStudent


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')


class SignupForm(forms.ModelForm):
    class Meta:
        model = PreStudent
        fields = ('first_name', 'phone', 'email')
