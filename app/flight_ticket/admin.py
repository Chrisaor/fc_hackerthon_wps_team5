from django.contrib import admin

from .models import FlightInfo, PriceInfo

admin.site.register(FlightInfo)
admin.site.register(PriceInfo)