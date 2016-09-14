from django.shortcuts import render
from django.utils import timezone
from django.http import HttpResponseRedirect
from .models import Character
from .forms import CharacterForm

# Create your views here.

def gochiusa(request):
    characters = Character.objects.all()
    return render(request, 'gochiusa.html', {'characters' : characters})

def character(request, name):
    character = Character.objects.get(name = name)
    return render(request, 'character.html', {'character' : character})

def character_post(request):
    if request.method == 'POST':
    	form = CharacterForm(request.POST)

    	if form.is_valid():
    		form.save()
    		return HttpResponseRedirect('/')

    else:
    	form = CharacterForm()

    return render(request, 'post.html', {'form' : form})