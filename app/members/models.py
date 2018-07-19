from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    CHOICE_GENDER = (
        ('m', '남성'),
        ('f', '여성'),
        ('x', '선택안함')
    )
    introduce = models.TextField(blank=True)
    gender = models.CharField(max_length=1, choices=CHOICE_GENDER)
    def __str__(self):
        return f'{self.username}'