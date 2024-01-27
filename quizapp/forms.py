from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import get_user_model
from django import forms
User = get_user_model()

class SignUP(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class QuizTypeForm(forms.Form):
    name = forms.CharField()


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
