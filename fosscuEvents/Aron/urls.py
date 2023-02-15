from django.urls import path
from . import views

urlpatterns = [
    path('events/', views.dashboard),
    path('RegisterEvent/', views.RegisterEvent, name="RegisterEvent")
]