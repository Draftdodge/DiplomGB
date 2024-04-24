import logging
from django.core.management.base import BaseCommand
from parkings.models import Client, Parking, ParkingSpots
from random import randint, uniform, choices
from datetime import date


logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fill parking'

    def add_arguments(self, parser):
        parser.add_argument('-p', '--p_id', type=int, help='ID Автостоянки')

    def handle(self, *args, **kwargs):

        p_id = kwargs.get('p_id')
        parking = Parking.objects.filter(pk=p_id).first()
        number_spot = parking.number_of_spot
        self.stdout.write(f' {number_spot=}')
        for i in range(number_spot):
             parking_spot = ParkingSpots(number_spot=(i+30), description='', price=f'{randint(1000, 5000)}',
                                         parking=parking)
             parking_spot.save()