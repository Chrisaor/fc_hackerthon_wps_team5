from django.db import models

from . import crawler


class FlightInfo(models.Model):
    CHOICE_DESTINATION = (
        ('osaa', '오사카'),
        ('tyoa', '도쿄'),
        ('bjsa', '베이징'),
        ('csha', '상하이'),
        ('tpet', '타이페이'),
        ('khh', '가오슝'),
        ('mfm', '마카오'),
        ('lpq', '루앙프라방'),
        ('vte', '비엔티엔'),
        ('bki', '코타키나발루'),
        ('kulm', '쿠알라룸프르'),
        ('pen', '페낭'),
        ('dad', '다낭'),
        ('sgn', '호치민'),
        ('han', '하노이'),
        ('dps', '발리'),
        ('cgki', '자카르타'),
        ('rep', '씨엠립'),
        ('pnh', '프놈펜'),
        ('bkkt', '방콕'),
        ('utp', '파타야'),
        ('syda', '시드니'),
        ('mela', '멜버른'),





    )
    origin = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True,)
    depart_month = models.IntegerField()

    def __str__(self):
        return f'{self.destination}행 {self.depart_month}월 티켓'

    def get_flight_info(self):
        flight_info = crawler.FlightInfo(
            origin=self.origin,
            destination=self.destination,
            month=self.depart_month)
        result = flight_info.skyscanner_flight_keyword_search()
        return result

    def get_price_info(self):
        for date_price in self.get_flight_info():
            PriceInfo.objects.create(flight=self ,date=date_price.date, price=date_price.price)


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

