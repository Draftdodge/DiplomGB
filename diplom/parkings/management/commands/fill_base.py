from django.core.management.base import BaseCommand
from parkings.models import Client, Parking, ParkingSpots
from random import randint, uniform, choices
from datetime import date


class Command(BaseCommand):
    help = 'Fill db by fake data'

    def handle(self, *args, **options):
        parkings = []
        for i in range(2):
            parking = Parking(name=f'Автостоянка{i+1}', reg_date=date(year=2024, month=randint(1, 8), day=randint(1, 26)),
                              description='', phone=f'{randint(10000000, 100000000)}', number_of_spot = 1,
                              )
            parking.save()
            parkings.append(parking)