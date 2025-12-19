from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import LoveMessage, GalleryImage


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/home/')

    if request.method == 'POST':
        user = authenticate(
            request,
            username=request.POST.get('username'),
            password=request.POST.get('password')
        )
        if user:
            login(request, user)
            return redirect('/home/')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('/')


@login_required
def home(request):
    return render(request, 'home.html')


@login_required
def birthday(request):
    return render(request, 'birthday.html')


@login_required
def ready(request):
    return render(request, 'ready.html')


@login_required
def message(request):
    msg = LoveMessage.objects.first()
    return render(request, 'message.html', {'msg': msg})


@login_required
def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery.html', {'images': images})
