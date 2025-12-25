from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User

def index(request):
    return render(request, 'main/index.html', {'title': "Главная страница"})

def about(request):
    return render(request, 'main/about.html', {'title': "Страница про нас"})

def contacts(request):
    return render(request, 'main/contacts.html', {'title': "Контакты"})

def user_register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password != password2:
            messages.error(request, 'Passwords do not match')
            return render(request, 'main/register.html')

        try:
            User.objects.create_user(username=username, password=password)
            messages.success(request, 'Registration successful! You can now log in.')
        except Exception as e:
            messages.error(request, f'Registration failed: {e}')
    return render(request, 'main/register.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'main/login.html')



def user_logout(request):
    pass