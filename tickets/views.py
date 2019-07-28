import requests
import json

from django.shortcuts import render
from django.http import HttpResponse
from tickets.models import Station


def shedule(request):
    return render(request, "tickets/shedule.html")


def get_city_list(request):
    city = request.GET.get('city').capitalize()
    cities = Station.objects.filter(station_name__istartswith=city)

    data = []
    for i in cities:
        data.append((i.station_number, i.station_name))

    return HttpResponse(json.dumps(data))


def time_arrival(request):
    departure_code = request.GET.get('departure_code')
    arrival_code = request.GET.get('arrival_code')

    r = requests.get(f"https://suggest.travelpayouts.com/search?service=tutu_trains&term={departure_code}&term2={arrival_code}",
                     headers={"Accept-Language": "ru"})
    data = r.json()['trips']

    return HttpResponse(json.dumps(data))
