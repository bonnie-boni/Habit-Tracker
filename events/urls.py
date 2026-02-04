from django.urls import path
from . import views

app_name = 'events'

urlpatterns = [
    path('log/', views.event_log, name='log'),
]
