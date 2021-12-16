from django.contrib.auth.models import User
from django.db import models


class ParkingSpace(models.Model):
    parking_space_number = models.PositiveIntegerField(verbose_name='Нормер парковочного места', unique=True)

    def __str__(self):
        return f'{self.parking_space_number}'


class ReservedPlace(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь забронированного места")
    parking_space = models.ForeignKey(ParkingSpace, on_delete=models.CASCADE, verbose_name='Парковочное место')
    date_start_parking = models.DateTimeField(verbose_name='Начало бронирования')
    date_finish_parking = models.DateTimeField(verbose_name='Окончание бронирования')
