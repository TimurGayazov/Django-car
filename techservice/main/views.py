from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home_page(request):
    user = request.user
    user_cars = Car.objects.filter(car_user=user)
    user_records = RecordMaintenance.objects.filter(record_user=user)
    context = {'user': user, 'user_cars': user_cars, 'user_records': user_records}
    return render(request, 'main/home.html', context)


def my_records(request):
    user = request.user
    user_records = RecordMaintenance.objects.filter(record_user=user).order_by('-record_maintenance_date')
    context = {'user': user, 'user_records': user_records}
    return render(request, 'main/my_records.html', context)


def my_cars(request):
    user = request.user
    user_cars = Car.objects.filter(car_user=user)
    context = {'user': user, 'user_cars': user_cars}
    return render(request, 'main/my_cars.html', context)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = RegisterForm()

    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("home")
    else:
        return render(request, "main/register.html", {"form": form})
