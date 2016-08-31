from django.shortcuts import render
from django.utils import timezone
from .models import Character

# Create your views here.

def gochiusa(request):
    characters = Character.objects.all()
    return render(request, 'gochiusa.html', {'characters' : characters})

def character(request, name):
    character = Character.objects.get(name = name)
    return render(request, 'character.html', {'character' : character})

def test(request):
    return render(request, 'test.html', {})
