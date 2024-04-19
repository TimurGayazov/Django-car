from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
from .models import *
from .forms import *


def home_page(request):
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        user = request.user
        user_cars = Car.objects.filter(car_user=user)
        user_records = RecordMaintenance.objects.filter(record_user=user)
        context = {'user': user, 'user_cars': user_cars, 'user_records': user_records}
        return render(request, 'main/home.html', context)
    else:
        context = {'error': 'Not logged in'}
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
            return redirect("login")
    else:
        form = RegisterForm()

    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/register.html", {"form": form})


def log_in(request):
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("profile")
    else:
        form = LoginForm()
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        return redirect("profile")
    else:
        return render(request, "main/login.html", {"form": form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('home')


def profile(request):
    if request.user.is_authenticated and request.user != 'AnonymousUser':
        user = request.user
        user_cars = Car.objects.filter(car_user=user)
        user_records = RecordMaintenance.objects.filter(record_user=user)
        context = {'user': user, 'user_cars': user_cars, 'user_records': user_records}
        return render(request, 'main/profile.html', context)
    else:
        return redirect('login')


def addrecord(request, pk):
    record_maintenance_type_get = request.GET.get('record_maintenance_type')
    record_maintenance_date_get = request.GET.get('record_maintenance_date')
    user_car = Car.objects.get(id=pk)
    types = TypeMaintenance.objects.all()
    if record_maintenance_type_get and record_maintenance_date_get:
        selected_type = TypeMaintenance.objects.filter(maintenance_name__icontains=str(record_maintenance_type_get))
        user = request.user
        record = RecordMaintenance.objects.get_or_create(record_user=user, record_maintenance_type=selected_type[0],
                                                         record_maintenance_date=record_maintenance_date_get,
                                                         record_car=user_car, record_car_mileage=user_car.car_mileage)[
            0]
        notification_mileage = user_car.car_mileage + selected_type[0].maintenance_mileage

        notification = Notification.objects.get_or_create(maintenance_type=selected_type[0], record_car=user_car,
                                                          car_mileage=notification_mileage)
        redirect_url = reverse('carrecords', kwargs={'pk': pk})
        return redirect(redirect_url)
    else:
        context = {'user_car': user_car, 'types': types}
        return render(request, 'main/addrecord.html', context)


def delrecord(request, pk):
    if request.user.is_authenticated:
        product = RecordMaintenance.objects.get(id=pk)
        product.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))


def carrecords(request, pk):
    user = request.user
    user_car = Car.objects.get(id=pk)
    notifications = Notification.objects.filter(record_car=user_car)
    user_records = RecordMaintenance.objects.filter(record_car=user_car).order_by('-record_maintenance_date')
    context = {'user_car': user_car, 'user_records': user_records, 'notifications': notifications}
    return render(request, 'main/carrecords.html', context)


class UpdateMileage(UpdateView):
    model = Car
    form_class = MileageForm
    template_name = 'main/update_mileage.html'
    success_url = reverse_lazy("my_cars")


def create_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)  # Создаем объект, но не сохраняем его в базу данных
            car.car_user = request.user  # Привязываем текущего пользователя к автомобилю
            car.save()  # Теперь сохраняем объект в базу данных
            return redirect('my_cars')  # Редиректим на страницу со списком автомобилей или куда угодно еще
    else:
        form = CarForm()
    return render(request, 'main/create_car.html', {'form': form})


def delcar(request, pk):
    if request.user.is_authenticated:
        user_car = Car.objects.get(id=pk)
        user_car.delete()
        return redirect('my_cars')
    else:
        return redirect('my_cars')


def delnotification(request, pk):
    if request.user.is_authenticated:
        notification = Notification.objects.get(id=pk)
        notification.delete()
        return redirect(request.META.get('HTTP_REFERER'))
    else:
        return redirect(request.META.get('HTTP_REFERER'))
