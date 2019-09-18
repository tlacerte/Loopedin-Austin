from django.urls import path
from . import views
from .views import EventsList

urlpatterns = [
  path('', views.home, name='index'),
  path('accounts/signup', views.signup, name='signup'),
  path('events/list', EventsList.as_view(), name='events_list'),
  path('events/create', views.show_event_create, name='show_event_create'),
  path('events/create/new', views.event_create, name='event_create'),
  path('events/<int:event_id>', views.event_detail, name='detail'),
  path('events/<int:pk>/update', views.UpdateEvent.as_view(), name='event_update'),
  path('events/<int:pk>/delete', views.DeleteEvent.as_view(), name='event_delete'),
  path('events/<int:event_id>/attend', views.event_attend, name='event_attend'),
  path('events/<int:event_id>/add_photo/', views.add_photo, name='add_photo'),
  path('user/my_events/', views.user_events, name='user_events_list'),
]