from django.http import HttpResponse
from django.shortcuts import render

from .models import FlightInfo, PriceInfo, Country, City


def country_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'flight_ticket/total.html', context)


def flight_main(request):
    return render(request, 'flight_ticket/search_flight.html')


def search_flight(request, origin, destination, month):
    instance = FlightInfo.objects.filter(destination=destination).filter(depart_month=month)
    if instance.exists():
        instance.delete()

    flight_info = FlightInfo.objects.create(origin=origin, destination=destination, depart_month=month)
    flight_info.get_price_info()
    flight = FlightInfo.objects.filter(destination=destination, depart_month=month).all()[0]

    prices = PriceInfo.objects.filter(flight__destination=destination, flight__depart_month=month)
    context = {
        'flight': flight,
        'prices': prices,
    }
    return render(request, 'flight_ticket/ticket_detail.html', context)


def flight_detail(request, pk):
    city = City.objects.get(pk=pk)
    context = {
        'city': city,
    }
    return render(request, 'main/flight_detail_barcelona.html', context)

def mel(request):
    return render(request, 'main/flight_detail_mel.html')

def bar(request):
    return render(request, 'main/flight_detail_barcelona.html')