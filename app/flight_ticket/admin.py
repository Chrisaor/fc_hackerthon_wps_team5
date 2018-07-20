from django.contrib import admin

from .models import FlightInfo, PriceInfo, Country, City

admin.site.register(FlightInfo)
admin.site.register(PriceInfo)
admin.site.register(Country)
admin.site.register(City)