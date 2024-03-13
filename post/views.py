from django.shortcuts import render
from .models import Pin

def index(request):
    pins = Pin.objects.all().order_by('-created')
    context = {
        'pins':pins
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    pin = Pin.objects.get(pk=pk)
    context = {
        'pin':pin
    }
    return render(request, 'post.html', context)  
