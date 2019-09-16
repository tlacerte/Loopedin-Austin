from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .forms import SignUpForm, CreateEventForm
from .models import Event, User

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

# def event_create(request):
#   event_form = CreateEventForm(request.POST)
#   if event_form.is_valid():
#     new_event = event_form.save(commit=False)
#     new_event.user_id = request.user.id
#     new_event.save()
#   return redirect('events_list')
class EventCreate(LoginRequiredMixin, CreateView):
  model = Event
  fields = ['name', 'date', 'category', 'location']
  def form_valid(self, form):
  # Assign the logged in user (self.request.user)
    form.instance.user = self.request.user
  # Let the CreateView do its job as usual
    return super().form_valid(form)  
  success_url = '/events/'

    
def event_detail(request, event_id):
  event = Event.objects.get(id=event_id)
  return render(request, 'events/detail.html', {'event': event})

  
