from django.shortcuts import render

from .models import FlightInfo, PriceInfo, Country


def country_list(request):
    countries = Country.objects.all()
    context = {
        'countries': countries,
    }
    return render(request, 'flight_ticket/total.html', context)


def flight_main(request):
    return render(request, 'flight_ticket/mainpage.html')

def search_flight(request):
    flight_info = FlightInfo.objects.create(origin='sela', destination='osaa', depart_month=7)
    flight_info.get_price_info()
    prices = PriceInfo.objects.all()
    context = {
        'prices': prices,
    }
    return render(request, 'flight_ticket/search_flight.html', context)

