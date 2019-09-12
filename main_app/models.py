from django.db import models
from django.urls import reverse
from datetime import date

CATEGORIES = ('Concert', 'Networking', 'Food/Drink', 'Market')

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('event date')
    category = models.CharField(
        max_length=30,
        choices=CATEGORIES
    ),
    location = models.CharField(max_length=100)

