from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.forms import TextInput, Textarea


def index(request):
    news = News.objects.order_by('-id')
    return render(request, 'main./index.html', {'title': 'Главная страница сайта', 'news': news})


def about(request):
    return render(request, 'main./about.html')


def e404(request):
    return render(request, 'main./e404.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была не верной'

    form = NewsForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main./create.html', context)


def user_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
    return render(request, 'main./create_user.html')


def user_logout(request):
    logout(request)
    return redirect('login_user')


def user_registration(request):
    error = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            error = 'Форма была неверно заполнена'

    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main./registration_user.html', context)


