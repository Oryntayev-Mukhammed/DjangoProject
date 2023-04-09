from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField, CaptchaTextInput

from .models import *


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class ContactForm(forms.Form):
    content = forms.CharField(label='Enter message', widget=forms.Textarea(attrs={
        'cols': 30, 'rows': 9, 'class': 'form-control w-100', 'onfocus': "'this.placeholder =''", 'placeholder': 'Enter message'
    }))
    name = forms.CharField(label='Enter your name', max_length=255, widget=forms.TextInput(attrs={
        'class': 'form-control valid', 'onfocus': "'this.placeholder =''", 'placeholder': 'Enter your name'
    }))
    email = forms.EmailField(label='Enter email address', widget=forms.EmailInput(attrs={
        'class': 'form-control valid', 'onfocus': "'this.placeholder =''", 'placeholder': 'Email'
    }))
    subject = forms.CharField(label='Enter Subject', widget=forms.TextInput(attrs={
        'class': 'form-control', 'onfocus': "'this.placeholder =''", 'placeholder': 'Enter Subject'
    }))
    captcha = CaptchaField(widget=CaptchaTextInput(attrs={
        'class': 'form-control w-25', 'onfocus': "'this.placeholder =''", 'placeholder': 'Captcha'
    }))
