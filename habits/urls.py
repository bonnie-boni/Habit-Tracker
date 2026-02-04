from django.urls import path
from . import views

app_name = 'habits'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('onboarding/', views.onboarding, name='onboarding'),
    path('read/', views.read_page, name='read_page'),
    path('watch/', views.video_watch, name='video_watch'),
]
