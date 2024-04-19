from .models import *
from django.forms import ModelForm, TextInput, DateTimeInput, EmailInput, PasswordInput, FileInput, FloatField, \
    CharField, ModelChoiceField
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from .models import *


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите username'}))
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите Имя'}))
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите Фамилию'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Введите email'}))
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Повторите пароль'}))
    role = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите роль'}), initial='User')

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password1", "password2", "role"]


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите username'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control", 'placeholder': 'Введите пароль'}))

    class Meta:
        model = User
        fields = ["username", "password"]


class MileageForm(ModelForm):
    car_mileage = forms.IntegerField(
        widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Введите пробег'}))

    class Meta:
        model = Car
        fields = ["car_mileage"]


class CarForm(forms.ModelForm):
    car_image = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'input-group form-control-file', 'type': 'file'}))
    car_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите название автомобиля'}))
    car_color = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Введите цвет автомобиля'}))
    car_mileage = forms.IntegerField(
            widget=forms.NumberInput(attrs={"class": "form-control", 'placeholder': 'Введите текущий пробег автомобиля'}))

    class Meta:
        model = Car
        fields = ['car_image', 'car_name', 'car_color', 'car_mileage']
        enctype = "multipart/form-data"

    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.car_user = user
        if commit:
            instance.save()
        return instance
