from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, PasswordInput, FileInput, FloatField, CharField, ModelChoiceField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the firstname'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the lastname'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Enter the email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Enter the password'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Repeat the password'}))
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Enter the role'}), initial='User')

    class Meta:
        model = User
        fields = ["username","first_name", "last_name", "email", "password1", "password2", "role"]
