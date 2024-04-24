from datetime import *

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import logging
from . import models
from . import forms
from .forms import ParkingsForm



logger = logging.getLogger(__name__)



def select_parking_spot(request, p_id):
    parking = models.Parking.objects.filter(pk=p_id).first()
    sp = {}
    for m in models.ParkingSpots.objects.filter(occupied=False, parking=parking):
        sp[m.number_spot] = (m.number_spot)
    if request.method == 'POST':
        form_ = ParkingsForm(request.POST)
        message = 'Ошибка в данных'
        if form_.is_valid():
            full_name = form_.cleaned_data['full_name']
            phone = form_.cleaned_data['phone']
            car_number = form_.cleaned_data['car_number']
            start_access_date = form_.cleaned_data['start_access_date']
            access_delta = form_.cleaned_data['access_delta']
            description = form_.cleaned_data['description']
            spot = request.POST.get("select_spots")
            parking_spot = models.ParkingSpots.objects.filter(parking_id=p_id, number_spot=spot).first()
            client = models.Client(full_name=full_name, phone=phone, car_number=car_number,
                                   start_access_date=start_access_date, end_access_date=access_delta,
                                   parking_spot=parking_spot, parking=parking, description=description)
            order = models.Order(client=client, parking_spot=parking_spot, parking=parking,
                                 start_access_date=start_access_date, end_access_date=access_delta, payment=False)
            logger.info(f'{spot=}')
            client.save()
            order.save()
            message = 'Заявка принята'
            form_ = forms.ParkingsForm()
    else:
        form_ = forms.ParkingsForm()
        message = 'Заполните форму'
    logger.info(f'{sp=}')
    return render(request, 'select_parking_spot.html', {'form': form_,
                                                        'parking': parking, 'message': message, 'sp': sp})

def get_all_parkings(request):
    parkings = models.Parking.objects.all()
    return render(request, 'parkings.html', {'parkings': parkings})

