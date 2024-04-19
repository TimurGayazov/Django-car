from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    role = models.CharField('Роль пользователя', max_length=200, default='User')


class Car(models.Model):
    car_image = models.ImageField('Изображение', upload_to='car_img/', null=True, blank=True)
    car_name = models.CharField('Название', max_length=100)
    car_color = models.CharField('Цвет', max_length=100)
    car_mileage = models.IntegerField('Текущий пробег', max_length=7, default=0)
    car_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.car_user} {self.car_name}'

    class Meta:
        verbose_name = 'Автомобиль'
        verbose_name_plural = 'Автомобили'


class TypeMaintenance(models.Model):
    maintenance_name = models.CharField('Название технического обслуживания', max_length=200)
    maintenance_mileage = models.IntegerField('Рекомендованная периодичность (пробег)', max_length=7, default=0)

    def __str__(self):
        return f'{self.maintenance_name}'

    class Meta:
        verbose_name = 'Вид технического обслуживания'
        verbose_name_plural = 'Виды технического обслуживания'


class RecordMaintenance(models.Model):
    record_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    record_maintenance_type = models.ForeignKey(TypeMaintenance, on_delete=models.CASCADE, null=True)
    record_maintenance_date = models.DateField('Дата технического обслуживания')
    record_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    record_car_mileage = models.IntegerField('Пробег автомобиля на данный момент', max_length=7, default=0)

    def __str__(self):
        return f'{self.record_car} {self.record_maintenance_type}'

    class Meta:
        verbose_name = 'Запись технического обслуживания'
        verbose_name_plural = 'Записи технического обслуживания'


class Notification(models.Model):
    maintenance_type = models.ForeignKey(TypeMaintenance, on_delete=models.CASCADE, null=True)
    record_car = models.ForeignKey(Car, on_delete=models.CASCADE, null=True)
    car_mileage = models.IntegerField('Пробег проведения тех. обслуживания', max_length=7, default=0)

    def __str__(self):
        return f'{self.record_car} {self.maintenance_type}'

    class Meta:
        verbose_name = 'Уведомление'
        verbose_name_plural = 'Уведомления'
