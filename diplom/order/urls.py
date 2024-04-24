from django.urls import path
from . import views


urlpatterns = [
    path('order_search/', views.order_search, name='order_search'),

]