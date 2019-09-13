from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import SignUpForm, CreateEventForm
from .models import Event

def home(request):
  return render(request, 'index.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = SignUpForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class EventsList(ListView):
  model = Event
  template_name = 'events/list.html'
  
class EventCreate(CreateView):
  model = Event
  create_event_form = CreateEventForm()
  success_url = '/events/list/'
  fields = ['name', 'date', 'category', 'location']