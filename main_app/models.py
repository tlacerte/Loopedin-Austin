from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

    
class Event(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField('event date')
    category = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'event_id': self.id})
    
class Attendee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={"pk": self.pk})

    
    
    def __str__(self):
        return self.event
    
class Photo(models.Model):
    url = models.CharField(max_length=200)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for event_id: {self.event_id} @{self.url}"
    