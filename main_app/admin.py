from django.contrib import admin
from .models import Event, Photo, Attendee

admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(Attendee)