from django.db import models

from . import crawler


class FlightInfo(models.Model):
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_month = models.IntegerField()

    def __str__(self):
        return f'{self.destination}행 티켓'

    def get_flight_info(self):
        flight_info = crawler.FlightInfo(
            origin=self.origin,
            destination=self.destination,
            month=self.depart_month)
        result = flight_info.skyscanner_flight_keyword_search()
        return result

    def get_price_info(self):
        for date_price in self.get_flight_info():
            PriceInfo.objects.create(date=date_price.date, price=date_price.price)


class PriceInfo(models.Model):
    flight = models.ForeignKey(FlightInfo, on_delete=models.CASCADE, null=True)
    date = models.IntegerField()
    price = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.date}일의 가격 : {self.price}'


class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

