from django.contrib.auth.models import AbstractUser
from django.db import models
# from ..flight_ticket.models import SingleTicket

class User(AbstractUser):
    CHOICE_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함')
    )
    introduce = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    # wish_list = models.ForeignKey(SingleTicket, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.username}'
