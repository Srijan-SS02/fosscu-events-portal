from django.urls import path
from . import views


urlpattern= [
    path('events/', views.dashboard, name='home'),
]