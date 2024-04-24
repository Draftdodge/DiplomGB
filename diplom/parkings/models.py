from django.db import models


class Parking(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название парковки')
    address = models.CharField(max_length=200, unique=True, verbose_name='Адрес парковки')
    number_of_spot = models.IntegerField(verbose_name='Количество мест')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    scheme = models.ImageField(null=True, verbose_name='Схема парковки')
    reg_date = models.DateField(auto_now=True, verbose_name='Дата регистрации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Парковка'
        verbose_name_plural = 'Парковки'

class ParkingSpots(models.Model):
    number_spot = models.IntegerField(verbose_name='Номер места')
    description = models.TextField(verbose_name='Описание места')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Стоимость места')
    occupied = models.BooleanField(default=False, verbose_name='Занято')
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, verbose_name='Парковка')

    def __str__(self):
        return f'{self.number_spot}'


class Client(models.Model):
    full_name = models.CharField(max_length=100, verbose_name='ФИО')
    description = models.TextField(max_length=1000, verbose_name='Описание')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    car_number = models.CharField(max_length=9, verbose_name='Номер автомобиля')
    key_number = models.IntegerField(default=0, verbose_name='Номер ключа')
    added_at = models.DateField(auto_now=True, verbose_name='Дата регистрации')
    access = models.BooleanField(default=False, verbose_name='Доступ')
    phone_access = models.BooleanField(default=False, verbose_name='Доступ по телефону')
    key_access = models.BooleanField(default=False, verbose_name='Доступ по ключу')
    start_access_date = models.DateField(auto_now=True, verbose_name='Дата начала доступа')
    end_access_date = models.DateField(verbose_name='Дата окончания доступа')
    parking_spot = models.ForeignKey(ParkingSpots, on_delete=models.CASCADE, verbose_name='Место')
    parking = models.ForeignKey(Parking, default=1, on_delete=models.CASCADE, verbose_name='Парковка')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')
    parking_spot = models.ForeignKey(ParkingSpots, on_delete=models.CASCADE, verbose_name='Место')
    parking = models.ForeignKey(Parking, on_delete=models.CASCADE, verbose_name='Парковка')
    start_access_date = models.DateField(auto_now=True, verbose_name='Дата начала доступа')
    end_access_date = models.DateField(verbose_name='Дата окончания доступа')
    payment = models.BooleanField(default=False, verbose_name='Оплачено')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'