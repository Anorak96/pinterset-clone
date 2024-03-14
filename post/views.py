from django.shortcuts import render
from .models import Pin, Tag, Board

def index(request):
    pins = Pin.objects.all().order_by('-created')
    tags = Tag.objects.all()[:4]
    context = {
        'pins': pins,
        'tags': tags
    }
    return render(request, 'index.html', context)

def detail(request, pk):
    pin = Pin.objects.get(pk=pk)
    context = {
        'pin':pin
    }
    return render(request, 'post.html', context)  

def tag(request, pk):
    tags = Pin.objects.filter(tag=pk)

    context = {
        'tags': tags,
    }
    return render(request, 'tag.html', context)

def board(request, name):
    board = Board.objects.filter(name=name)
    context = {
        'board': board
    }
    return render(request, 'board.html', context)