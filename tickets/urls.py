from django.urls import path
from tickets.views import *


urlpatterns = [
    path('shedule/', shedule, name='tickets_shedule'),
    path('get_city_list/', get_city_list, name='get_city_list'),
    path('time_arrival/', time_arrival, name='time_arrival'),
]



