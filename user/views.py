from django.shortcuts import render
from .models import User
from post.models import Pin

def profile(request, username):
    user = User.objects.get(username=username)
    pictures = Pin.objects.filter(profile=user).order_by('-created')

    context = {
        'user': user,
        'pictures': pictures
    }
    return render(request, 'author.html', context)