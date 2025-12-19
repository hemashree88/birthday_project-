from django.shortcuts import render
from .models import LoveMessage, GalleryImage

def home(request):
    return render(request, 'home.html')

def birthday(request):
    return render(request, 'birthday.html')

def ready(request):
    return render(request, 'ready.html')

def message(request):
    msg = LoveMessage.objects.first()
    return render(request, 'message.html', {'msg': msg})

def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})
