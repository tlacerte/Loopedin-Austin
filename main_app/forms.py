from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import User, Event

class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username']
        
class CreateEventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'date', 'category', 'location']
        