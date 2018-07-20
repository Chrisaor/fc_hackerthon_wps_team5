from django.db import models

from . import crawler


class FlightInfo(models.Model):
    SEAT_CLASS = (
        ('F', '일등석'),
        ('N', '일반석'),
        ('B', '비지니스석'),
        ('P', '프리미엄 일반석'),
    )
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_date = models.DateField(blank=True)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.destination}행 티켓'

    def get_flight_info(self, month):
        flight_info = crawler.FlightInfo(
            origin=self.origin,
            destination=self.destination,
            month=month)
        print(flight_info)


    def get_price_info(self):
        price_info = crawler.PriceInfo(date=self.depart_date, price=self.price)
        print(price_info)


class FlightTicket(models.Model):
    pass

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'

