from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import SignUpForm, CreateEventForm
import uuid
import boto3
from .models import Event, User, Photo

S3_BASE_URL = 'https://s3-us-west-1.amazonaws.com/'
BUCKET = 'loopedin'

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

def show_event_create(request):
  user = User.objects.get(id=request.user.id)
  return render(request, 'events/create.html')

def event_create(request):
  event_form = CreateEventForm(request.POST)
  if event_form.is_valid():
    new_event = event_form.save(commit=False)
    new_event.user_id = request.user.id
    new_event.save()
  return redirect('events_list')

def event_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  return render(request, 'events/detail.html', { 'event': event })

class UpdateEvent(UpdateView):
  model = Event
  fields = ['name', 'date', 'category', 'location']
  success_url = '/events/list'

class DeleteEvent(DeleteView):
  model = Event
  fields = ['name', 'date', 'category', 'location']
  success_url = '/events/list'
  
def add_photo(request, event_id):
  photo_file = request.FILES.get('photo-file', None)
  if photo_file:
    s3 = boto3.client('s3')
    key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
    try:
      s3.upload_fileobj(photo_file, BUCKET, key)
      url = f"{S3_BASE_URL}{BUCKET}/{key}"
      photo = Photo(url=url, event_id=event_id)
      photo.save()
    except:
      print('An error occurred uploading file to S3')
  return redirect('detail', event_id=event_id)