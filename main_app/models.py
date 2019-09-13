from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


CATEGORIES = (
    ('concert', 'Concert'),
    ('networking', 'Networking'),
    ('food-drink', 'Food/Drink'),
    ('market', 'Market')
)

class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('event date')
    category = models.CharField(
        max_length=100,
        choices=CATEGORIES,
        default=CATEGORIES[0][0]
    )
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})