from django.shortcuts import redirect, render

from flight_ticket.models import Country, City


def index(request):
    cities = City.objects.all()
    context = {
        'cities': cities
    }
    return render(request, 'main/mainpage.html', context)
