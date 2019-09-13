from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

CATEGORIES = ('Concert', 'Networking', 'Food/Drink', 'Market')

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('event date')
    category = models.CharField(
        max_length=30,
        choices=CATEGORIES
    ),
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    
