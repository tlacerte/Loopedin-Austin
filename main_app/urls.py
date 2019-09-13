from django.urls import path
from . import views
from .views import EventsList, EventCreate

urlpatterns = [
  path('', views.home, name='home'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/list', EventsList.as_view(), name='events_list'),
  path('events/create', EventCreate.as_view(), name='event_create'),
  path('events/<int:event_id>', views.event_detail, name='detail'),
]