from django.shortcuts import render
from django.utils import timezone
from .models import Character

# Create your views here.

def gochiusa(request):
    characters = Character.objects.all()
    return render(request, 'gochiusa.html', {'characters' : characters})

def chino(request):
    chino = Character.objects.get(name = 'chino')
    return render(request, 'chino.html', {'chino' : chino})
