from django.db import models

class SingleTicket(models.Model):
    SEAT_CLASS = (
        ('F', '일등석'),
        ('N', '일반석'),
        ('B', '비지니스석'),
        ('P', '프리미엄 일반석'),
    )
    departure = models.CharField(max_length=200, blank=True)
    destination = models.CharField(max_length=200, blank=True)
    depart_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True)
    seat_class = models.CharField(max_length=200, choices=SEAT_CLASS)
    adult = models.IntegerField()
    children = models.IntegerField()
    infants = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return f'{self.destination}행 티켓'

