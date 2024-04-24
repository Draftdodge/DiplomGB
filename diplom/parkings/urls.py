from django.urls import path
from . import views


urlpatterns = [
    path('parkings/', views.get_all_parkings, name='parkings'),
    path('select_parking_spot/<int:p_id>/', views.select_parking_spot, name='select_parking_spot'),

]

