from django.urls import path
from . import views

app_name = 'content'

urlpatterns = [
    path('', views.content_list, name='list'),
    path('<int:id>/', views.content_detail, name='detail'),
]
