from django.shortcuts import render

from .models import FlightInfo, PriceInfo


def flight_main(request):
    return render(request, 'flight_ticket/mainpage.html')

def search_flight(request):
    flight_info = FlightInfo.objects.create(origin='sela', destination='osaa', depart_month=7)
    flight_info.get_price_info()
    prices = PriceInfo.objects.all()
    context = {
        'prices':prices,
    }
    return render(request, 'flight_ticket/ticket_detail.html', context)

