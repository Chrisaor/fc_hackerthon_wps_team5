from django.db import models

class FlightTicket(models.Model):
    SEAT_CLASS = (
        ('F', '일등석'),
        ('N', '일반석'),
        ('B', '비지니스석'),
        ('P', '프리미엄 일반석'),
    )
    departure = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_date = models.DateField(blank=True)
    price = models.IntegerField()

    class Meta:
        abstract = True

class SingleTicket(FlightTicket):

    def __str__(self):
        return f'{self.destination}행 티켓'

class RoundTicket(FlightTicket):
    return_date = models.DateField(blank=True)

    def __str__(self):
        return f'{self.destination}행 티켓'

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.name}'

class City(models.Model):
    name = models.CharField(max_length=100)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}'



