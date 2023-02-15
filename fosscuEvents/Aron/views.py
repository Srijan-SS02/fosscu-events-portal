from django.shortcuts import render, redirect
from .forms import *


# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html') 


def RegisterEvent(request):
    form=RegisterEventform()

    if request.method=='POST':
        form=RegisterEventform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/fosscu/events')
      
    return render(request, 'RegisterEvent.html',{
        "form":form
    })