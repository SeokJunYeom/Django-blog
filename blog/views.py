from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

def gochiusa(request):
    posts = Post.objects.all()
    return render(request, 'gochiusa.html', {'characters' : posts})
